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

@repeat(3)
def mul_2(i: 'Int') -> 'int':
	return i * 2

print(mul_2(3))
