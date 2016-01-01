Getting Started 
========

Installation
------------

* Install NeoDjango with your favorite Python package manager:
	
	pip install neodjango

* Downloaded and run Neo4j 
	
	- http://neo4j.com/download/
	- http://neo4j.com/docs/stable/server-installation.html


Configuration
-------------

Once you’ve installed neodjango and configure your Django project for connect to Neo4j.

Database Setup
==============

An example settings.py::
	
	INSTALLED_APPS = (
	    # other apps
	    "neodjango",
	)

   	NEO4J_DATABASES = {
        'default' : {
            'HOST':'localhost',
            'PORT':7474,
            'ENDPOINT':'/db/data'
        }
    }