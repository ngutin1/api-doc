Members Endpoint
================

Retrieve information about NY Assembly members.

List All Members
----------------

Get a list of all assembly members with optional filtering.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /members

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
   * - ``session_year``
     - integer
     - No
     - Filter by session year (e.g., 2021, 2023, 2025)
   * - ``district``
     - integer
     - No
     - Filter by district number (1-150)
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

   curl "http://nyassembly.duckdns.org:8888/members?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

With Python:

.. code-block:: python

   import requests
   
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/members",
       params={
           "key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU",
           "session_year": 2025,
           "limit": 50
       }
   )
   
   data = response.json()

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "member-session list",
       "total": 236,
       "offsetStart": 1,
       "offsetEnd": 50,
       "limit": 50,
       "result": {
           "items": [
               {
                   "sessionMemberId": 502,
                   "shortName": "ABBATE",
                   "sessionYear": 2021,
                   "districtCode": 49,
                   "alternate": false,
                   "memberId": 502
               },
               {
                   "sessionMemberId": 622,
                   "shortName": "ABINANTI",
                   "sessionYear": 2021,
                   "districtCode": 92,
                   "alternate": false,
                   "memberId": 622
               }
           ]
       }
   }

Response Fields
~~~~~~~~~~~~~~~

* ``sessionMemberId``: Unique identifier for this member in this session
* ``shortName``: Member's last name in uppercase
* ``sessionYear``: Year of the session (2019, 2021, 2023, 2025)
* ``districtCode``: Assembly district number (1-150)
* ``alternate``: Whether this is an alternate member (always false)
* ``memberId``: Unique member identifier across all sessions

Get Specific Member
-------------------

Retrieve details for a specific member by ID.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /members/{member_id}

Parameters
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Required
     - Description
   * - ``member_id``
     - integer
     - Yes
     - Member ID (in URL path)
   * - ``key``
     - string
     - Yes
     - Your API key

Example Request
~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/members/502?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

With Python:

.. code-block:: python

   import requests
   
   member_id = 502
   response = requests.get(
       f"http://nyassembly.duckdns.org:8888/members/{member_id}",
       params={"key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"}
   )
   
   data = response.json()

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "member",
       "total": 1,
       "offsetStart": 1,
       "offsetEnd": 1,
       "limit": 1,
       "result": {
           "sessionMemberId": 502,
           "shortName": "ABBATE",
           "sessionYear": 2021,
           "districtCode": 49,
           "alternate": false,
           "memberId": 502
       }
   }

Member Not Found
~~~~~~~~~~~~~~~~

If the member doesn't exist:

.. code-block:: json

   {
       "success": false,
       "message": "Member not found",
       "responseType": "member",
       "total": 0,
       "offsetStart": 0,
       "offsetEnd": 0,
       "limit": 1,
       "result": {}
   }

Common Use Cases
----------------

Find Members by District
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all members from district 49
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/members",
       params={
           "key": API_KEY,
           "district": 49
       }
   )

Find Members by Session Year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all members from 2025 session
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/members",
       params={
           "key": API_KEY,
           "session_year": 2025
       }
   )

Paginate Through All Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_all_members(api_key):
       """Retrieve all members with pagination"""
       all_members = []
       offset = 0
       limit = 400
       
       while True:
           response = requests.get(
               "http://nyassembly.duckdns.org:8888/members",
               params={
                   "key": api_key,
                   "limit": limit,
                   "offset": offset
               }
           )
           
           data = response.json()
           members = data['result']['items']
           all_members.extend(members)
           
           if offset + len(members) >= data['total']:
               break
           
           offset += limit
       
       return all_members

Rate Limits
-----------

* 60 requests per minute per IP address

See :doc:`../rate-limits` for more information.
