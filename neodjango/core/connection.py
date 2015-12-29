from __future__ import unicode_literals

from ..utils import URLConnection
from neo4jrestclient.client import GraphDatabase

def Connection():
	return GraphDatabase(URLConnection())