Segments Endpoint
=================

Retrieve parsed transcript segments - individual statements made by assembly members during floor proceedings.

List Segments
-------------

Get a list of transcript segments with optional filtering.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /segments

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
   * - ``date``
     - string
     - No
     - Filter by date (YYYY-MM-DD format)
   * - ``member_id``
     - integer
     - No
     - Filter by member ID
   * - ``limit``
     - integer
     - No
     - Number of results per page (default: 100, max: 1000)
   * - ``offset``
     - integer
     - No
     - Number of results to skip (default: 0)

Example Request
~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/segments?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU&date=2025-06-15"

With Python:

.. code-block:: python

   import requests
   
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/segments",
       params={
           "key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU",
           "date": "2025-06-15",
           "limit": 50
       }
   )
   
   data = response.json()
   for segment in data['result']['items']:
       print(f"{segment['memberName']}: {segment['text'][:100]}...")

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "segment list",
       "total": 342,
       "offsetStart": 1,
       "offsetEnd": 50,
       "limit": 50,
       "result": {
           "items": [
               {
                   "segmentId": 15234,
                   "date": "2025-06-15",
                   "sequenceNumber": 1,
                   "memberId": 535,
                   "text": "ACTING SPEAKER AUBRY: The House will come to order.",
                   "memberName": "AUBRY"
               },
               {
                   "segmentId": 15235,
                   "date": "2025-06-15",
                   "sequenceNumber": 2,
                   "memberId": 535,
                   "text": "In the absence of clergy, let us pause for a moment of silence.",
                   "memberName": "AUBRY"
               }
           ]
       }
   }

Response Fields
~~~~~~~~~~~~~~~

* ``segmentId``: Unique identifier for this segment
* ``date``: Date of the transcript (YYYY-MM-DD)
* ``sequenceNumber``: Order in which this segment appeared (1-indexed)
* ``memberId``: ID of the member who spoke (null if unidentified speaker)
* ``text``: The actual statement/text
* ``memberName``: Name of the member (null if unidentified speaker)

Get Specific Segment
--------------------

Retrieve a single segment by ID.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /segments/{segment_id}

Parameters
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Required
     - Description
   * - ``segment_id``
     - integer
     - Yes
     - Segment ID (in URL path)
   * - ``key``
     - string
     - Yes
     - Your API key

Example Request
~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/segments/15234?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

With Python:

.. code-block:: python

   import requests
   
   segment_id = 15234
   response = requests.get(
       f"http://nyassembly.duckdns.org:8888/segments/{segment_id}",
       params={"key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"}
   )
   
   data = response.json()

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "segment",
       "total": 1,
       "offsetStart": 1,
       "offsetEnd": 1,
       "limit": 1,
       "result": {
           "segmentId": 15234,
           "date": "2025-06-15",
           "sequenceNumber": 1,
           "memberId": 535,
           "text": "ACTING SPEAKER AUBRY: The House will come to order.",
           "memberName": "AUBRY"
       }
   }

Segment Not Found
~~~~~~~~~~~~~~~~~

If the segment doesn't exist:

.. code-block:: json

   {
       "success": false,
       "message": "Segment not found",
       "responseType": "segment",
       "total": 0,
       "offsetStart": 0,
       "offsetEnd": 0,
       "limit": 1,
       "result": {}
   }

Common Use Cases
----------------

Get All Segments for a Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_all_segments_for_date(date, api_key):
       """Retrieve all segments from a specific date"""
       all_segments = []
       offset = 0
       limit = 1000
       
       while True:
           response = requests.get(
               "http://nyassembly.duckdns.org:8888/segments",
               params={
                   "key": api_key,
                   "date": date,
                   "limit": limit,
                   "offset": offset
               }
           )
           
           data = response.json()
           segments = data['result']['items']
           all_segments.extend(segments)
           
           if offset + len(segments) >= data['total']:
               break
           
           offset += limit
       
       return all_segments
   
   segments = get_all_segments_for_date("2025-06-15", API_KEY)
   print(f"Total segments: {len(segments)}")

Get All Statements by a Member
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_member_statements(member_id, api_key, start_date=None):
       """Get all statements by a specific member"""
       params = {
           "key": api_key,
           "member_id": member_id,
           "limit": 1000
       }
       
       if start_date:
           params["date"] = start_date
       
       response = requests.get(
           "http://nyassembly.duckdns.org:8888/segments",
           params=params
       )
       
       return response.json()['result']['items']
   
   # Get all statements by member 535 (AUBRY)
   statements = get_member_statements(535, API_KEY)
   print(f"Member made {len(statements)} statements")


Advantages Over Full Transcripts
---------------------------------

Using segments instead of full transcripts provides:

* **Structured data**: Each statement is a separate record
* **Speaker attribution**: Know who said what
* **Easier filtering**: Filter by member or date
* **Smaller responses**: Retrieve only what you need
* **Sequential ordering**: Segments are numbered in order

Rate Limits
-----------

* 60 requests per minute per IP address

See :doc:`../rate-limits` for more information.

Related Endpoints
-----------------

* :doc:`members` - Get information about assembly members
* :doc:`transcripts` - Get full, unparsed transcripts
* :doc:`interactions` - Analyze member-to-member interactions within segments
