#!/usr/local/bin/python3.6

def repeat(n: 'int'):
	def decorator(func):
		def repeated_func(arg):
			res = arg
			k = n
			while (k > 0):
				res = func(res)
				k -= 1
			return res 
		return repeated_func
	return decorator
 
