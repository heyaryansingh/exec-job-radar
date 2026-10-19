# JSearch test (1 API call)

- /search: HTTP 404 '{"message":"Endpoint \'\\/search\' does not exist"}'
- /search-v2: HTTP 200 '{"status":"OK","request_id":"598cb329-9ce6-40e6-a5ce-de1237542044","parameters":{"query":"'
HTTP 200 via /search-v2
- x-ratelimit-requests-limit: 200
- x-ratelimit-requests-remaining: 197

Response shape: dict keys ['status', 'request_id', 'parameters', 'data']
```
{"status":"OK","request_id":"598cb329-9ce6-40e6-a5ce-de1237542044","parameters":{"query":"vice president technology in USA","num_pages":1,"date_posted":"week","country":"us","language":"en"},"data":{"jobs":[{"job_id":"ZlZrT2VZUE5WblBYNjNZbkFBQUFBQT09OkVzd0JDb3dCUVVwcFZEUjBTMFJ0WTJoRFRtbHBaMEZxTUdkTWVHRnZSbGcwV1RsUlNVbENVMjFCTFU1alJuQnJiMmh2VlZwNmRGaDFOVFYzUkV4ZkxXOUxWVWRsTjBGTmQxUjBVSEZ0UjJWQldrRn
```

Script error:
```
Traceback (most recent call last):
  File "/home/runner/work/exec-job-radar/exec-job-radar/tools/test_jsearch.py", line 67, in <module>
    pubs = collections.Counter(j.get("job_publisher") for j in data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/collections/__init__.py", line 607, in __init__
    self.update(iterable, **kwds)
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/collections/__init__.py", line 699, in update
    _count_elements(self, iterable)
  File "/home/runner/work/exec-job-radar/exec-job-radar/tools/test_jsearch.py", line 67, in <genexpr>
    pubs = collections.Counter(j.get("job_publisher") for j in data)
                               ^^^^^
AttributeError: 'str' object has no attribute 'get'

```
