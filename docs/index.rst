NY Assembly Transcript API Documentation
=========================================

Welcome to the NY Assembly Transcript API - a comprehensive database of New York State Assembly floor transcripts, members, and legislative interactions.

.. note::
   **Demo API Key**: ``drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU``
   
   Use this key for testing and development. Include it in all requests: ``?key=YOUR_KEY``

.. raw:: html

   <div style="background-color: #e7f3e7; padding: 15px; border-radius: 5px; margin: 20px 0;">
       <h3 style="margin-top: 0;">🟢 API Status</h3>
       <p><strong>Base URL:</strong> <code>http://nyassembly.duckdns.org:8888</code></p>
       <p><strong>Status:</strong> <span style="color: green; font-weight: bold;">● Online</span></p>
       <p><strong>Version:</strong> 1.0</p>
   </div>

Quick Start
-----------

Make your first API call:

.. code-block:: bash

   curl "http://nyassembly.duckdns.org:8888/members?key=drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"

Or with Python:

.. code-block:: python

   import requests
   
   API_KEY = "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"
   BASE_URL = "http://nyassembly.duckdns.org:8888"
   
   response = requests.get(f"{BASE_URL}/members?key={API_KEY}")
   data = response.json()
   print(data)

Features
--------

* **Assembly Members**: Complete roster with district and session information
* **Floor Transcripts**: Full text of assembly floor proceedings
* **Transcript Segments**: Parsed individual statements by members
* **Interaction Analysis**: Member-to-member interactions with sentiment analysis
* **Rate Limiting**: 60 requests/minute for most endpoints
* **Pagination**: Efficient data retrieval with offset/limit parameters

Data Coverage
-------------

The API currently includes:

* Assembly sessions from 2019-2025
* 236+ assembly members (current and former)
* Complete floor transcripts
* Parsed interactions including questions, responses, and acknowledgments
* Sentiment analysis on member interactions

Infrastructure
--------------

This API is deployed on a self-hosted Ubuntu server using:

* **FastAPI**: Modern Python web framework
* **PostgreSQL**: Relational database for structured legislative data

The server runs as a systemd service, ensuring the API automatically restarts on failure and starts on system boot. This provides reliable 24/7 availability without requiring containerization.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   
   getting-started
   authentication
   rate-limits

.. toctree::
   :maxdepth: 2
   :caption: API Reference
   
   endpoints/members
   endpoints/transcripts
   endpoints/segments
   endpoints/interactions

.. toctree::
   :maxdepth: 2
   :caption: Additional Resources
   
   examples
   

GitHub Repository
-----------------

View the source code: `NY Assembly Transcript API <https://github.com/ngutin1/ny-assembly-api>`_


Support
-------

For questions or issues:

* Check the :doc:`examples` page for common use cases
* Open an issue on GitHub

References & Acknowledgments
=============================

This project was built using the following technologies and resources:

Frameworks & Libraries
----------------------

* **FastAPI** - Modern Python web framework for building APIs
  
  * Documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/
  * Used for: Core API framework, automatic API documentation, request validation

* **SQLModel** - SQL database integration for FastAPI
  
  * Documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/#install-sqlmodel
  * Used for: Database ORM, data models, PostgreSQL integration

* **Requests** - HTTP library for Python
  
  * Documentation: https://requests.readthedocs.io/en/latest/user/quickstart/
  * Used for: Testing API endpoints, making HTTP requests

* **PyPDF2** - PDF text extraction library
  
  * Documentation: https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html
  * Used for: Extracting text from assembly transcript PDFs

* **Psycopg** - PostgreSQL adapter for Python
  
  * Documentation: https://www.psycopg.org/docs/
  * Used for: PostgreSQL database connections and operations

* **SlowAPI** - Rate limiting for FastAPI
  
  * Documentation: https://slowapi.readthedocs.io/en/latest/
  * Used for: Implementing rate limiting on API endpoints

Infrastructure Services
-----------------------

* **DuckDNS** - Free dynamic DNS service
  
  * Website: https://www.duckdns.org/domains
  * Used for: Providing stable domain name (nyassembly.duckdns.org) for dynamic IP

Data Sources
------------

* **New York State Assembly** - Official transcript source
  
  * Transcripts: https://nyassembly.gov/av/session/
  * Used for: Source of all floor session transcripts and legislative data

* **New York State Senate Open Legislation API** - API design reference
  
  * Documentation: https://legislation.nysenate.gov/static/docs/html/index.html
  * Used for: API structure inspiration and response format guidance

Learning Resources
------------------

* **Design of Web APIs** by Arnaud Lauret
  
  * Used for: API design principles, REST best practices, endpoint structure

* **Creating First REST API with FastAPI** - GeeksforGeeks Tutorial
  
  * Tutorial: https://www.geeksforgeeks.org/python/creating-first-rest-api-with-fastapi/
  * Used for: Initial FastAPI setup and learning

Special Thanks
--------------

* **New York State Assembly** for providing public access to legislative transcripts
* **Read the Docs** for documentation hosting

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
