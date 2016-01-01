from __future__ import unicode_literals

from six import with_metaclass

from manager import Manager
from options import Options

class ModelBase(type):
	def __new__(cls, name, bases, attrs):
		"""
		Also ensure initialization is only performed for subclasses of Model,
        excluding Model class itself).
		"""
		parents = [b for b in bases if isinstance(b, ModelBase)]
		if not parents:
			return super(ModelBase, cls).__new__(cls, name, bases, attrs)

		module = attrs.pop('__module__')
		attr_meta = attrs.pop('Meta', None)
		
		new_class = type.__new__(cls, name, bases, {'__module__': module})
		
		if not attr_meta:
			meta = getattr(new_class, 'Meta', None)
		else:
			meta = attr_meta
        
		new_class.add_to_class('_meta', Options(meta))	
		new_class.add_to_class('objects', Manager())

		return new_class

	def add_to_class(cls, name, value):
		if hasattr(value, 'contribute_to_class'):
			value.contribute_to_class(cls, name)
		else:
			setattr(cls, name, value)
		
class Node(with_metaclass(ModelBase)):
	pass