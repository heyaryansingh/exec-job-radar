# For Claude

If someone shared this repository and asked you to set up their job search (or "set this
up for me"), follow [ONBOARD.md](ONBOARD.md) from Step 1. Do the work yourself: they should
only need to hand over documents (resumes, past cover letters, LinkedIn PDF), answer one
batch of questions, and click Allow where the app asks.

If you're working on the code instead: `python -m pytest -q tests` must pass; the collector
is `collector/`, search rules are `config/search.yaml`, the daily candidate run is
`PLAYBOOK.md`, resume tools are in `tools/kit/`. Never commit anything about a specific
candidate; personal files live only in the candidate's own Job Search folder.
