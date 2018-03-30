#coding:utf_8

import threading

class Singlen(type):
	_instances = {}
	_instance_lock = threading.Lock()
	def __call__(cls, *args, **kwargs):
		with Singlen._instance_lock:
			if cls not in cls._instances:
				cls._instances[cls] = super(Singlen, cls).__call__(*args, **kwargs)
			return cls._instances[cls]

class S1(metaclass=Singlen):
	pass

class S2(metaclass=Singlen):
	pass

if __name__ == '__main__':
	s1 = S1()
	s2 = S1()
	print(id(s1))
	print(id(s2))

