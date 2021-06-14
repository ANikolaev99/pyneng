#!/usr/bin/env python
from sys import argv
text = argv[1:]
text = ''.join(text)
with open('config_sw1.txt') as config:
	for line in config:
		if '!' in line[0]:
			continue
		else:
			print(line.rstrip())


