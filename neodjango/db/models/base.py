from __future__ import unicode_literals


class ManagerBaseQuerySet(object):
	def all(self):
		return self.__class__.__name__

class BaseQuerySet(object):
	objects = ManagerBaseQuerySet()

	def __init__(self):
		pass

class Node(BaseQuerySet):
	pass