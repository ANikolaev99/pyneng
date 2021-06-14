#!/usr/bin/env python

vlan = input('Введите номер VLAN: ')
with open('CAM_table.txt') as config:
	lists = []
	for line in config:
		try:
			int(line.split()[0])
		except (ValueError, IndexError):
			continue
		else:
			line = line.split()
			line.pop(-2)
			lists.append(line)
	lists.sort()
	for item in lists:
		if vlan == item[0]:
			print(item[0] + '	' + item[1] + '	' + item[2])


#with open('CAM_table.txt', 'r') as start:
#	lists = []
#	for line in start:
#		if line.count('.') is 2:
#			a = line.strip('\n').split() 
#			a.pop(-2)
#			lists.append(a) 
#	lists.sort()
#	for l in lists:
#		print(l[0] + '    ' + l[1] + '   ' + l[2])


