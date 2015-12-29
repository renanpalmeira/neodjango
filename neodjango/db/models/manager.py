from __future__ import unicode_literals

from neodjango.core.connection import Connection

class Manager(object):

	def __init__(self, *args, **kwargs):
		self.graph = Connection()

	def __repr__(self):
		return '<Node: {0} >'.format(self.graph.labels.get(self.model))

	def all(self):
		return self.graph.labels.get(self.model)