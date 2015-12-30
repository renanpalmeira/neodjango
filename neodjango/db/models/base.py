from __future__ import unicode_literals

from six import with_metaclass

from .manager import Manager 

class ModelBase(type):
	def __new__(cls, name, bases, attrs):
		super_class = super(ModelBase, cls).__new__

		module = attrs.pop('__module__')
		new_class = super_class(cls, name, bases, {'__module__': module})
		new_class.add_to_class(cls, 'objects', Manager(name))
		
		return super_class(cls, name, bases, attrs)

	def add_to_class(self, cls, name, value):
		setattr(cls, name, value)


class Node(with_metaclass(ModelBase)):
	pass