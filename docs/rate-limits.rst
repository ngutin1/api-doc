Rate Limits
===========

The API implements rate limiting to ensure fair usage and system stability.

Rate Limit Tiers
----------------

Different endpoints have different rate limits:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Endpoint
     - Rate Limit
     - Window
   * - ``/`` (root)
     - 100 requests
     - per minute
   * - ``/members``
     - 60 requests
     - per minute
   * - ``/members/{id}``
     - 60 requests
     - per minute
   * - ``/transcripts``
     - 60 requests
     - per minute
   * - ``/transcripts/{date}``
     - 30 requests
     - per minute
   * - ``/segments``
     - 60 requests
     - per minute
   * - ``/segments/{id}``
     - 60 requests
     - per minute
   * - ``/interactions``
     - 60 requests
     - per minute
   * - ``/interactions/{id}``
     - 60 requests
     - per minute

How Rate Limiting Works
------------------------

Rate limits are applied per IP address. Each request decrements your available quota for that endpoint. The quota resets after the time window expires.

Example: If you make 60 requests to ``/members`` in one minute, the 61st request will be rate limited. After one minute, your quota resets.

Rate Limit Headers
------------------

Currently, rate limit information is not returned in response headers. When you exceed the rate limit, you'll receive a 429 Too Many Requests response.

Rate Limit Exceeded Response
----------------------------

When you exceed the rate limit:

.. code-block:: json

   {
       "error": "Rate limit exceeded"
   }

HTTP Status Code: ``429 Too Many Requests``

Best Practices
--------------

Implement Exponential Backoff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you receive a 429 response, wait before retrying:

.. code-block:: python

   import requests
   import time
   
   def make_request_with_retry(url, params, max_retries=3):
       for attempt in range(max_retries):
           response = requests.get(url, params=params)
           
           if response.status_code == 429:
               # Exponential backoff: 1s, 2s, 4s
               wait_time = 2 ** attempt
               print(f"Rate limited. Waiting {wait_time} seconds...")
               time.sleep(wait_time)
               continue
           
           return response
       
       raise Exception("Max retries exceeded")


