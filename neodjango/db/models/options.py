from __future__ import unicode_literals

class Options(object):
	def __init__(self, meta, *args, **kwargs):
	    self.meta = meta

	def __getitem__(self, value):
		if hasattr(self.meta, value):
			return getattr(self.meta, value, 'url')
		return None