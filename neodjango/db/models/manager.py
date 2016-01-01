import inspect
import six

from query import QuerySet

class BaseManager(object):
	
	def __init__(self):
		super(BaseManager, self).__init__()
		self.node = None

	def __str__(self):
		return '<Neo4j Node: {0}>'.format(self.node)

	def contribute_to_class(self, node, name):
		self.node = node
		setattr(node, name, self)

	@classmethod
	def _get_queryset_methods(cls, queryset_class):
		def create_method(name, method):
			def manager_method(self, *args, **kwargs):
				return getattr(self.get_queryset(), name)(*args, **kwargs)
			manager_method.__name__ = method.__name__
			manager_method.__doc__ = method.__doc__
			return manager_method
		
		new_methods = {}
		
		predicate = inspect.isfunction if six.PY3 else inspect.ismethod
		for name, method in inspect.getmembers(queryset_class, predicate=predicate):
			
			if hasattr(cls, name):
				continue
			
			queryset_only = getattr(method, 'queryset_only', None)
			if queryset_only or (queryset_only is None and name.startswith('_')):
				continue
			
			new_methods[name] = create_method(name, method)

		return new_methods

	def get_queryset(self):
		return self._queryset_class(cls_=self.node)
        
	@classmethod
	def from_queryset(cls, queryset_class, class_name=None):
		if class_name is None:
			class_name = '%sFrom%s' % (cls.__name__, queryset_class.__name__)
		class_dict = {
			'_queryset_class': queryset_class,
		}
		class_dict.update(cls._get_queryset_methods(queryset_class))
		return type(class_name, (cls,), class_dict)

class Manager(BaseManager.from_queryset(QuerySet)):
	pass