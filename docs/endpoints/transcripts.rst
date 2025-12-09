Transcripts Endpoint
====================

Retrieve full floor transcripts from NY Assembly sessions.

List All Transcript Dates
--------------------------

Get a list of all available transcript dates.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /transcripts

Parameters
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Required
     - Description
   * - ``key``
     - string
     - Yes
     - Your API key
   * - ``limit``
     - integer
     - No
     - Number of results per page (default: 400, max: 1000)
   * - ``offset``
     - integer
     - No
     - Number of results to skip (default: 0)

Example Request
~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/transcripts?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

With Python:

.. code-block:: python

   import requests
   
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/transcripts",
       params={
           "key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU",
           "limit": 100
       }
   )
   
   data = response.json()
   for item in data['result']['items']:
       print(item['date'])

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "transcript list",
       "total": 427,
       "offsetStart": 1,
       "offsetEnd": 100,
       "limit": 100,
       "result": {
           "items": [
               {"date": "2025-06-15"},
               {"date": "2025-06-14"},
               {"date": "2025-06-13"},
               {"date": "2025-05-22"}
           ]
       }
   }

Response Fields
~~~~~~~~~~~~~~~

* ``date``: Date of the transcript in YYYY-MM-DD format

.. note::
   Dates are returned in descending order (most recent first).

Get Specific Transcript
-----------------------

Retrieve the full text of a transcript for a specific date.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /transcripts/{date}

Parameters
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Required
     - Description
   * - ``date``
     - string
     - Yes
     - Date in YYYY-MM-DD format (in URL path)
   * - ``key``
     - string
     - Yes
     - Your API key

Example Request
~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/transcripts/2025-06-15?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

With Python:

.. code-block:: python

   import requests
   
   date = "2025-06-15"
   response = requests.get(
       f"http://nyassembly.duckdns.org:8888/transcripts/{date}",
       params={"key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"}
   )
   
   data = response.json()
   transcript_text = data['result']['text']

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "transcript",
       "total": 1,
       "offsetStart": 1,
       "offsetEnd": 1,
       "limit": 1,
       "result": {
           "date": "2025-06-15",
           "text": "ACTING SPEAKER AUBRY: The House will come to order. In the absence of clergy, let us pause for a moment of silence..."
       }
   }

Response Fields
~~~~~~~~~~~~~~~

* ``date``: Date of the transcript in YYYY-MM-DD format
* ``text``: Full transcript text (can be very long, 50,000+ characters)

Transcript Not Found
~~~~~~~~~~~~~~~~~~~~

If no transcript exists for the specified date:

.. code-block:: json

   {
       "success": false,
       "message": "Transcript not found",
       "responseType": "transcript",
       "total": 0,
       "offsetStart": 0,
       "offsetEnd": 0,
       "limit": 1,
       "result": {}
   }

.. warning::
   Full transcript responses can be large (50KB-500KB). Consider using the :doc:`segments` endpoint for parsed, manageable chunks instead.

Common Use Cases
----------------

Find Available Dates
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all available transcript dates
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/transcripts",
       params={
           "key": API_KEY,
           "limit": 1000
       }
   )
   
   dates = [item['date'] for item in response.json()['result']['items']]
   print(f"Available transcripts: {len(dates)}")
   print(f"Most recent: {dates[0]}")
   print(f"Oldest: {dates[-1]}")

Download Transcript for Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import requests
   
   def download_transcript(date, api_key):
       """Download and save a transcript"""
       response = requests.get(
           f"http://nyassembly.duckdns.org:8888/transcripts/{date}",
           params={"key": api_key}
       )
       
       data = response.json()
       
       if not data['success']:
           print(f"Transcript not found for {date}")
           return None
       
       # Save to file
       filename = f"transcript_{date}.txt"
       with open(filename, 'w', encoding='utf-8') as f:
           f.write(data['result']['text'])
       
       print(f"Saved transcript to {filename}")
       return data['result']['text']
   
   transcript = download_transcript("2025-06-15", API_KEY)

Search Transcript Text
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def search_transcript(date, search_term, api_key):
       """Search for a term in a transcript"""
       response = requests.get(
           f"http://nyassembly.duckdns.org:8888/transcripts/{date}",
           params={"key": api_key}
       )
       
       data = response.json()
       
       if not data['success']:
           return []
       
       text = data['result']['text']
       lines = text.split('\n')
       
       # Find lines containing the search term
       matches = [line for line in lines if search_term.lower() in line.lower()]
       
       return matches
   
   # Search for mentions of "budget"
   results = search_transcript("2025-06-15", "budget", API_KEY)
   print(f"Found {len(results)} mentions of 'budget'")

Bulk Download Transcripts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import time
   
   def download_all_transcripts(api_key, start_date=None, end_date=None):
       """Download all transcripts within a date range"""
       # Get all dates
       response = requests.get(
           "http://nyassembly.duckdns.org:8888/transcripts",
           params={"key": api_key, "limit": 1000}
       )
       
       dates = [item['date'] for item in response.json()['result']['items']]
       
       # Filter by date range if provided
       if start_date:
           dates = [d for d in dates if d >= start_date]
       if end_date:
           dates = [d for d in dates if d <= end_date]
       
       transcripts = {}
       
       for date in dates:
           print(f"Downloading transcript for {date}...")
           
           response = requests.get(
               f"http://nyassembly.duckdns.org:8888/transcripts/{date}",
               params={"key": api_key}
           )
           
           data = response.json()
           if data['success']:
               transcripts[date] = data['result']['text']
           
           # Be nice to the server (rate limit is 30/min for this endpoint)
           time.sleep(2)
       
       return transcripts
   
   # Download all transcripts from June 2025
   transcripts = download_all_transcripts(
       API_KEY,
       start_date="2025-06-01",
       end_date="2025-06-30"
   )

Rate Limits
-----------

* ``/transcripts`` (list): 60 requests per minute per IP address
* ``/transcripts/{date}`` (specific): **30 requests per minute** per IP address

.. note::
   The specific transcript endpoint has a lower rate limit because responses are large. Plan accordingly for bulk downloads.

See :doc:`../rate-limits` for more information.

Alternative: Use Segments
-------------------------

For most use cases, consider using the :doc:`segments` endpoint instead:

* Returns parsed, structured data instead of raw text
* Links statements to specific members
* Supports filtering by member and date
* More efficient for analysis
* Smaller response sizes

See :doc:`segments` for details.
