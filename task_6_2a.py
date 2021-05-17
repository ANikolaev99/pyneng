#!/usr/bin/env python

ip = input('Введите IP-адрес в формате 10.0.1.1: ')

# Проверка
if '.' in ip and len(ip.split('.')) == 4:
	for num in range(4):
		if int(ip.split('.')[num]) >= 0 and int(ip.split('.')[num]) <= 255:
			if int(ip.split('.')[0]) > 0 and int(ip.split('.')[0]) < 224:
				print('тип IP-адреса unicast')
				break
			elif int(ip.split('.')[0]) > 223 and int(ip.split('.')[0]) < 240:
				print('тип IP-адреса multicast')
				break
			elif ip in '255.255.255.255':
				print('тип IP-адреса local broadcast')
				break
			elif ip in '0.0.0.0':
				print('тип IP-адреса unassigned')
				break
			else:
				print('тип IP-адреса unused')
				break
		else:
			print('Неправильный IP-адрес')
			break
else:
	print('Неправильный IP-адрес')

