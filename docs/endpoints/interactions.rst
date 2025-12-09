Interactions Endpoint
=====================

Retrieve member-to-member interactions identified in floor transcripts. Interactions include questions, responses, acknowledgments, and other exchanges between assembly members.

List Interactions
-----------------

Get a list of interactions with optional filtering.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /interactions

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
   * - ``member_id``
     - integer
     - No
     - Filter by member ID (returns interactions involving this member)
   * - ``date``
     - string
     - No
     - Filter by date (YYYY-MM-DD format)
   * - ``interaction_type``
     - string
     - No
     - Filter by interaction type (question, response, acknowledgment, etc.)
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

   curl "http://nyassembly.duckdns.org:8888/interactions?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU&date=2025-06-15"

With Python:

.. code-block:: python

   import requests
   
   response = requests.get(
       "http://nyassembly.duckdns.org:8888/interactions",
       params={
           "key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU",
           "date": "2025-06-15",
           "limit": 50
       }
   )
   
   data = response.json()
   for interaction in data['result']['items']:
       print(f"{interaction['fromMemberName']} -> {interaction['toMemberName']}: {interaction['interactionType']}")

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "interaction list",
       "total": 128,
       "offsetStart": 1,
       "offsetEnd": 50,
       "limit": 50,
       "result": {
           "items": [
               {
                   "activityId": 5421,
                   "date": "2025-06-15",
                   "segmentId": 15250,
                   "memberFrom": 519,
                   "memberTo": 535,
                   "interactionType": "question",
                   "fromMemberName": "GLICK",
                   "toMemberName": "AUBRY",
                   "sentiment": "neutral"
               },
               {
                   "activityId": 5422,
                   "date": "2025-06-15",
                   "segmentId": 15251,
                   "memberFrom": 535,
                   "memberTo": 519,
                   "interactionType": "response",
                   "fromMemberName": "AUBRY",
                   "toMemberName": "GLICK",
                   "sentiment": "positive"
               }
           ]
       }
   }

Response Fields
~~~~~~~~~~~~~~~

* ``activityId``: Unique identifier for this interaction
* ``date``: Date of the interaction (YYYY-MM-DD)
* ``segmentId``: ID of the transcript segment where this occurred
* ``memberFrom``: ID of the member initiating the interaction
* ``memberTo``: ID of the member receiving the interaction
* ``interactionType``: Type of interaction (question, response, acknowledgment, objection, etc.)
* ``fromMemberName``: Name of the initiating member
* ``toMemberName``: Name of the receiving member
* ``sentiment``: Sentiment analysis (positive, negative, neutral)

Interaction Types
~~~~~~~~~~~~~~~~~

Common interaction types include:

* ``question`` - Member asks a question
* ``response`` - Member responds to a question
* ``acknowledgment`` - Member acknowledges another member
* ``objection`` - Member objects to something
* ``point_of_order`` - Member raises a point of order
* ``clarification`` - Member seeks or provides clarification

Get Specific Interaction
-------------------------

Retrieve a single interaction by ID.

Endpoint
~~~~~~~~

.. code-block:: text

   GET /interactions/{activity_id}

Parameters
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Required
     - Description
   * - ``activity_id``
     - integer
     - Yes
     - Activity/Interaction ID (in URL path)
   * - ``key``
     - string
     - Yes
     - Your API key

Example Request
~~~~~~~~~~~~~~~

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/interactions/5421?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

With Python:

.. code-block:: python

   import requests
   
   activity_id = 5421
   response = requests.get(
       f"http://nyassembly.duckdns.org:8888/interactions/{activity_id}",
       params={"key": "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"}
   )
   
   data = response.json()

Example Response
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "success": true,
       "message": "",
       "responseType": "interaction",
       "total": 1,
       "offsetStart": 1,
       "offsetEnd": 1,
       "limit": 1,
       "result": {
           "activityId": 5421,
           "date": "2025-06-15",
           "segmentId": 15250,
           "memberFrom": 519,
           "memberTo": 535,
           "interactionType": "question",
           "fromMemberName": "GLICK",
           "toMemberName": "AUBRY",
           "sentiment": "neutral"
       }
   }

Interaction Not Found
~~~~~~~~~~~~~~~~~~~~~

If the interaction doesn't exist:

.. code-block:: json

   {
       "success": false,
       "message": "Interaction not found",
       "responseType": "interaction",
       "total": 0,
       "offsetStart": 0,
       "offsetEnd": 0,
       "limit": 1,
       "result": {}
   }

Common Use Cases
----------------

Find Member's Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_member_interactions(member_id, api_key):
       """Get all interactions involving a member"""
       response = requests.get(
           "http://nyassembly.duckdns.org:8888/interactions",
           params={
               "key": api_key,
               "member_id": member_id,
               "limit": 1000
           }
       )
       
       return response.json()['result']['items']
   
   # Get all interactions involving member 519 (GLICK)
   interactions = get_member_interactions(519, API_KEY)
   print(f"Found {len(interactions)} interactions")

Use Cases
---------

This endpoint enables analysis of:

* **Member relationships**: Who interacts with whom most frequently
* **Communication patterns**: Which members ask the most questions
* **Network analysis**: Visualize interaction networks
* **Legislative dynamics**: Understand debate patterns and alliances

Rate Limits
-----------

* 60 requests per minute per IP address

See :doc:`../rate-limits` for more information.

Related Endpoints
-----------------

* :doc:`members` - Get information about assembly members
* :doc:`segments` - View the actual text of segments where interactions occurred
* :doc:`transcripts` - Get full transcripts containing these interactions
