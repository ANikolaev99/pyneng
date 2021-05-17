#!/usr/bin/env python

ip = input('Введите IP-адрес в формате 10.0.1.1: ')

if int(ip.split('.')[0]) > 0 and int(ip.split('.')[0]) < 224:
	print('тип IP-адреса unicast')
elif int(ip.split('.')[0]) > 223 and int(ip.split('.')[0]) < 240:
	print('тип IP-адреса multicast')
elif ip in '255.255.255.255':
	print('тип IP-адреса local broadcast')
elif ip in '0.0.0.0':
	print('тип IP-адреса unassigned')
else:
	print('тип IP-адреса unused')

