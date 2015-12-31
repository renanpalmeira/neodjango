from __future__ import unicode_literals

from neodjango.core.connection import Connection

class Manager(object):

	def __init__(self, cls, *args, **kwargs):
		self.graph = Connection()
		self.cls_ = cls

	def __repr__(self):
		return '<Node: {0} >'.format(self.graph.labels.get(self.cls_))

	def all(self):
		return self.graph.labels.get(self.cls_)