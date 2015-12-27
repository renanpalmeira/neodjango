from __future__ import unicode_literals

from ..utils import URLConnection
from neo4jrestclient.client import GraphDatabase


class Connection(GraphDatabase):

	def __init__(self, *args, **kwargs):
		self._url = URLConnection()
		super(GraphDatabase, self).__init__(self, self._url, *args, **kwargs)
