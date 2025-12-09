Examples
========

Complete code examples for common use cases.

Basic Data Retrieval
--------------------

Get All Members
~~~~~~~~~~~~~~~

.. code-block:: python

   import requests
   
   API_KEY = "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"
   BASE_URL = "http://nyassembly.duckdns.org:8888"
   
   response = requests.get(
       f"{BASE_URL}/members",
       params={"key": API_KEY}
   )
   
   data = response.json()
   print(f"Total members: {data['total']}")
   
   for member in data['result']['items']:
       print(f"{member['shortName']} - District {member['districtCode']}")

Get Transcript for Specific Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   date = "2025-06-15"
   
   response = requests.get(
       f"{BASE_URL}/transcripts/{date}",
       params={"key": API_KEY}
   )
   
   data = response.json()
   
   if data['success']:
       print(f"Transcript length: {len(data['result']['text'])} characters")
       print(data['result']['text'][:500])  # Print first 500 chars
   else:
       print(f"Error: {data['message']}")

