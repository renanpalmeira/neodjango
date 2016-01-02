from __future__ import unicode_literals

from unittest import TestCase

class NeoDjangoTest(TestCase):
	def setUp(self):
		self.node = True

	def test_node(self):
		self.assertEqual(self.node, True)