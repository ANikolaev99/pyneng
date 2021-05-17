#!/usr/bin/env python
result = 0
while result == 0:
	ip = input('Введите IP-адрес в формате 10.0.1.1: ')

	# Проверка
	if '.' in ip and len(ip.split('.')) == 4:
		for num in range(4):
			if int(ip.split('.')[num]) >= 0 and int(ip.split('.')[num]) <= 255:
				if int(ip.split('.')[0]) > 0 and int(ip.split('.')[0]) < 224:
					print('тип IP-адреса unicast')
					result = 1
					break
				elif int(ip.split('.')[0]) > 223 and int(ip.split('.')[0]) < 240:
					print('тип IP-адреса multicast')
					result = 1
					break
				elif ip in '255.255.255.255':
					print('тип IP-адреса local broadcast')
					result = 1
					break
				elif ip in '0.0.0.0':
					print('тип IP-адреса unassigned')
					result = 1
					break
				else:
					print('тип IP-адреса unused')
					result = 1
					break
			else:
				print('Неправильный IP-адрес')
				result = 0
				break
	else:
		print('Неправильный IP-адрес')
		result = 0


