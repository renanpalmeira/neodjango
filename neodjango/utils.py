from __future__ import unicode_literals

from django.conf import settings as _settings

def URLConnection():
	try:
		if not 'NEO4J_DATABASES' in dir(_settings):
			raise Exception("Not have 'NEO4J_DATABASES' in settings.py. Read more: http://goo.gl/TnbmHo/")
		
		if not type(_settings.NEO4J_DATABASES) is dict:
			raise Exception("NEO4J_DATABASES is not configured correctly in settings.py. Read more: http://goo.gl/TnbmHo/")

		if not 'default' in _settings.NEO4J_DATABASES.keys():
			raise Exception("NEO4J_DATABASES is not configured correctly in settings.py. Read more: http://goo.gl/TnbmHo/")
		
		_default = _settings.NEO4J_DATABASES['default']
		
		if not 'HOST' in _default \
			and not 'PORT' in _default \
			and not 'ENDPOINT' in _default:
			raise Exception("NEO4J_DATABASES is not configured correctly in settings.py. Read more: http://goo.gl/TnbmHo/")

		protocol = "http"
		host = _default['HOST']
		port = _default['PORT']
		endpoint = _default['ENDPOINT']

		_url = "%s://%s:%s%s" % (protocol, host, port, endpoint)
		return _url
	except Exception, e:
		raise e