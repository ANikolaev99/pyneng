#!/usr/bin/env python

import subprocess
list_of_ips = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1'] #списаок ip адресов

def ping_ip_addresses(list_of_ips):
	"""
	Сама функкция для выполнения задания

	"""
	available = []
	not_available = []
	for ip in list_of_ips:
		reply = subprocess.run(['ping', '-c', '2', ip])
		if reply.returncode == 0:
			available.append(ip)
		else:
			not_available.append(ip)
	list_result = [available, not_available]
	print('РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ, {} \n кортеж списков доступных и не доступных IP'
					.format(tuple(list_result)))

ping_ip_addresses(list_of_ips) #вызов функции



