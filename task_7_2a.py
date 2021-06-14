#!/usr/bin/env python

from sys import argv
text = argv[1:]
text = ''.join(text)
ignore = ['duplex', 'alias', 'Current configuration']
with open(text) as config:
	for line in config:
		if ignore[0] in line or ignore[1] in line or ignore[2] in line or '!' in line:
			continue
		else:
			 print(line.rstrip())

