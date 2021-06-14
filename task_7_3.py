#!/usr/bin/env python

with open('CAM_table.txt') as config:
	for line in config:
		try:
			int(line.split()[0])
		except (ValueError, IndexError):
			continue
		else:
			print(line)

