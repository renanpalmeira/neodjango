from __future__ import unicode_literals, with_statement

import os
import codecs
import re

from django.core.management.base import BaseCommand, CommandError
from neodjango.core.connection import Connection

class Command(BaseCommand):
	help = 'Closes the specified poll for voting'

	def add_arguments(self, parser):
		parser.add_argument('-l', '--load', action='store')

	def handle(self, *args, **options):
		if 'load' in options and not options['load'] is None and os.path.isfile(options['load']):
			load = options['load']
			gdb = Connection()

			with codecs.open(load, 'rb', encoding='utf-8') as file_load:
				cypher = file_load.read()

			"""
			the dump cyphers by Neo4j, always starting with 'begin' and end 'commit', for now
			the lib of used in background not read this words
			"""
			cypher = re.sub(r'(begin|commit)', '', cypher)
			gdb.query(q=cypher)
			self.stdout.write("LOAD {0} - OK".format(load))
