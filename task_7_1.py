#!/usr/bin/env python
with open('ospf.txt', 'r') as f:
	for line in f:
		result = '''
		Protocol: 	   	OSPF
		Prefix:             	{}
		AD/Metric: 		{}
		Next-Hop: 		{}
		Last update: 		{}
		Outbound Interface: 	{}
		'''
		print(result.format(
					line.split()[1],
					line.split()[2],
					line.split()[4],
					line.split()[5],
					line.split()[6]))


