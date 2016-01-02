Nodes
=====

Model
-----

* Writing nodes.py
	
	from neodjango.db import models

	class Label(models.Model):
		class Meta:
			display = "name"


Querying
--------

* Retrieving all objects

	>>> Label.objects.all()
	[<Node#id: property>, <Node#id: property>, <Node#id: property>, <Node#id: property>]

* Retrieving specific objects with filters

	>>> Label.objects.filter(name='Guido')
	[<Node#id: property>,]

* Retrieving a single object with get

	>>> Label.objects.get(name='Lawrence')
	<Node#id: property>

	>>> Label.objects.get(id=42)
	<Node#id: property>