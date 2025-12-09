Getting Started
===============

This guide will help you make your first requests to the NY Assembly Transcript API.

Base URL
--------

All API requests should be made to:

.. code-block:: text

   http://nyassembly.duckdns.org:8888

Demo API Key
------------

For testing and development, use this demo key:

.. code-block:: text

   drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU

Include it in all requests as a query parameter: ``?key=YOUR_KEY``

Making Your First Request
--------------------------

Command Line (curl)
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/members?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

Python
~~~~~~

.. code-block:: python

   import requests
   
   API_KEY = "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"
   BASE_URL = "http://nyassembly.duckdns.org:8888"
   
   # Get all members
   response = requests.get(f"{BASE_URL}/members", params={"key": API_KEY})
   
   if response.status_code == 200:
       data = response.json()
       print(f"Total members: {data['total']}")
       for member in data['result']['items'][:5]:
           print(f"  - {member['shortName']} (District {member['districtCode']})")
   else:
       print(f"Error: {response.status_code}")

JavaScript (Node.js)
~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   const axios = require('axios');
   
   const API_KEY = 'drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU';
   const BASE_URL = 'http://nyassembly.duckdns.org:8888';
   
   async function getMembers() {
       try {
           const response = await axios.get(`${BASE_URL}/members`, {
               params: { key: API_KEY }
           });
           
           console.log(`Total members: ${response.data.total}`);
           response.data.result.items.slice(0, 5).forEach(member => {
               console.log(`  - ${member.shortName} (District ${member.districtCode})`);
           });
       } catch (error) {
           console.error('Error:', error.message);
       }
   }
   
   getMembers();

R
~

.. code-block:: r

   library(httr)
   library(jsonlite)
   
   API_KEY <- "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"
   BASE_URL <- "http://nyassembly.duckdns.org:8888"
   
   # Get members
   response <- GET(
       paste0(BASE_URL, "/members"),
       query = list(key = API_KEY)
   )
   
   data <- content(response, as = "parsed")
   cat("Total members:", data$total, "\n")

Understanding the Response
---------------------------

All successful responses follow this structure:

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "member-session list",
       "total": 236,
       "offsetStart": 1,
       "offsetEnd": 236,
       "limit": 400,
       "result": {
           "items": [...]
       }
   }

Response Fields
~~~~~~~~~~~~~~~

* ``success`` (boolean): Whether the request succeeded
* ``message`` (string): Error message if request failed, empty on success
* ``responseType`` (string): Type of data returned
* ``total`` (integer): Total number of items available
* ``offsetStart`` (integer): Starting position in results (1-indexed)
* ``offsetEnd`` (integer): Ending position in results
* ``limit`` (integer): Maximum items per page
* ``result`` (object): Contains the actual data in ``items`` array

Pagination
----------

Most endpoints support pagination using ``limit`` and ``offset`` parameters:

.. code-block:: python

   # Get first 50 members
   response = requests.get(
       f"{BASE_URL}/members",
       params={
           "key": API_KEY,
           "limit": 50,
           "offset": 0
       }
   )
   
   # Get next 50 members
   response = requests.get(
       f"{BASE_URL}/members",
       params={
           "key": API_KEY,
           "limit": 50,
           "offset": 50
       }
   )

Default and Maximum Limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Most endpoints: ``limit=100`` (default), ``limit=1000`` (maximum)
* ``/members``: ``limit=400`` (default), ``limit=1000`` (maximum)
* ``/transcripts``: ``limit=400`` (default), ``limit=1000`` (maximum)

Next Steps
----------

* Learn about :doc:`authentication` and API keys
* Understand :doc:`rate-limits` to avoid throttling
* Explore the :doc:`endpoints/members` endpoint
* See more :doc:`examples` for common use cases
