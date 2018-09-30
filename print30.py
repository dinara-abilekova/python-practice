"""
Имитация большинства особенностей функции print 
в версии 3.0 для использования с интерпретатором версии 2.Х
Сигнатура вызова: print30(*ars, sep=' ', end='\n', file=None)
"""
import sys

def print30(*args, **kargs):
	sep = kargs.get('sep', ' ')
	end = kargs.get('end', '\n')
	file = kargs.pop('file', sys.stdout)
	if kargs: raise TypeError('extra keywords: %s' % kargs)
	output = ''
	first = True
	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output + end)