from django import template

register = template.Library()

def hash(h, key):
	if str(key) in h:
		return h[str(key)]
	else:
		return None


register.filter('hash', hash)

