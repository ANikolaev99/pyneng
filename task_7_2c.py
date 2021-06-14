#!/usr/bin/env python

from sys import argv
text = argv[1:]
a = text[0]
b = text[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(a) as config:
	for line in config:
		if ignore[0] in line or ignore[1] in line or ignore[2] in line:
			continue
		else:
			f = open(b, 'a+')
			f.write(line)

