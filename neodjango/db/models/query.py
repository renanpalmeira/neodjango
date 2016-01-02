# -*- coding: utf-8 -*-

from neodjango.core.connection import Connection

class NodeRelationshipQuerySet(object):

	def __init__(self, relationship, *args, **kwargs):
		self.relationship = relationship

	def __repr__(self):
		_id_relationship = self.relationship.id
		_display = self.relationship.url
		
		return '<Relationship#{0}: {1}>'.format(_id_relationship, _display)

	def __getattr__(self, name, *args, **kwargs):
		if name in self.relationship.end.properties:
			return self.relationship.end.properties[name]
		raise KeyError("Relationship#{0} has no property {1}. Read more: http://goo.gl/TnbmHo/".format(self.relationship.id, name))

	@classmethod
	def _create_relationship(self):
		pass

class NodeQuerySet(object):
	PROPERTY = None
	RELATIONSHIP_TEXT = lambda self, text: text.upper()

	def __init__(self, node, *args, **kwargs):
		self.node = node

	def __getattr__(self, name, *args, **kwargs):
		if name in self.node.properties:
			return self.node.properties[name]
		else:
			name = self.RELATIONSHIP_TEXT(name)
			def wrapper(*args, **kwargs):
				relationships = self.node.relationships.all(types=[name])
				return [NodeRelationshipQuerySet(relationship) for relationship in relationships]
			return wrapper

	def __len__(self):
		return 1

	def __repr__(self):
		_id_node = self.node.id
		_display = self.node.url
		
		if not self.PROPERTY is None:
			_display = self.node.properties[self.PROPERTY].encode('ascii', 'ignore')
		
		return '<Node#{0}: {1}>'.format(_id_node, _display)

	def relationships(self):
		relationships = self.node.relationships.all()
		return [NodeRelationshipQuerySet(relationship) for relationship in relationships]


class QuerySet(object):
	def __init__(self, cls_, *args, **kwargs):
		self.graph = Connection()
		self.cls_ = cls_
		if not self.cls_._meta['label'] is None:
			self._nodes_by_labels = self.graph.labels.get(self.cls_._meta['label'])
			self.label = self.cls_._meta['label']
		else:
			self._nodes_by_labels = self.graph.labels.get(self.cls_.__name__)
			self.label = self.cls_.__name__

		if not self.cls_._meta['display'] is None:
			NodeQuerySet.PROPERTY = self.cls_._meta['display']
		
	def _node_filter(self, **kwargs):
		result = [NodeQuerySet(node) for node in self._nodes_by_labels.get(**kwargs)]
		result.reverse()
		return result

	def _node_get(self, id_node):
		result = self.graph.nodes.get(id_node)
		return NodeQuerySet(result)

	def _node_all(self):
		return self._node_filter()

	def filter(self, **kwargs):
		return self._node_filter(**kwargs)

	def get(self, **kwargs):
		if 'id' in kwargs.keys():
			result = self._node_get(kwargs['id'])
		else:
			result = self._node_filter(**kwargs)
			result = result[0]

		if len(result)!=1:
			raise ValueError("None has no property. Read more: http://goo.gl/TnbmHo/")
		return result
	
	def all(self):
		return self._node_all()