Authentication
==============

All API requests require authentication using an API key.

API Key
-------

Include your API key in every request as a query parameter:

.. code-block:: text

   ?key=YOUR_API_KEY

Demo Key
--------

For testing and development:

.. code-block:: text

   drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU

Example Request
---------------

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/members?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

