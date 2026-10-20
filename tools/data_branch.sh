#!/usr/bin/env bash
# The large JSON files the collector rewrites every hour live on a separate `data` branch
# that is replaced (force-pushed) on every run, so it never builds up history and the
# repository stays small. The readable pages (README.md, data/*.md) stay on main.
#
#   tools/data_branch.sh restore   copy the files from origin/data into data/ (no staging)
#   tools/data_branch.sh save      publish data/*.json as one fresh commit on `data`
#
# Raw URL for readers: https://raw.githubusercontent.com/<owner>/<repo>/data/data/apply_queue.json
set -euo pipefail
FILES="data/roles.json data/latest.json data/apply_queue.json data/state.json data/health.json data/board_names.json data/auto_boards.json"

case "${1:-}" in
  restore)
    rc=0; git ls-remote --exit-code -q origin data >/dev/null 2>&1 || rc=$?
    if [ "$rc" -ne 0 ] && [ "$rc" -ne 2 ]; then echo "could not reach origin"; exit 1; fi
    if [ "$rc" -eq 0 ]; then
      # The branch exists: it must restore, or the run would overwrite the database with
      # a near-empty one. Fail the step instead (save then refuses, see below).
      for i in 1 2 3; do
        git fetch -q --depth=1 origin data && git archive FETCH_HEAD data | tar -x && break
        [ "$i" -eq 3 ] && { echo "could not restore the data branch"; exit 1; }
        sleep $((i * 5))
      done
      echo "restored data files from the data branch"
    else
      echo "no data branch yet; starting from whatever is in data/"
    fi
    touch data/.restored
    ;;
  save)
    [ -e data/.restored ] || { echo "restore did not succeed this run; not saving"; exit 1; }
    export GIT_INDEX_FILE="$(mktemp -u)"
    git read-tree --empty
    n=0
    for f in $FILES; do
      if [ -s "$f" ]; then git add -f "$f"; n=$((n + 1)); fi
    done
    if [ "$n" -eq 0 ]; then echo "nothing to save"; rm -f "$GIT_INDEX_FILE"; exit 0; fi
    tree=$(git write-tree)
    commit=$(echo "data: $(date -u +'%Y-%m-%d %H:%M') UTC" | git commit-tree "$tree")
    rm -f "$GIT_INDEX_FILE"; unset GIT_INDEX_FILE
    for i in 1 2 3; do
      git push -q -f origin "$commit:refs/heads/data" && { echo "saved $n files to the data branch"; exit 0; }
      sleep $((i * 5))
    done
    exit 1
    ;;
  *) echo "usage: $0 restore|save"; exit 2 ;;
esac
