#!/usr/bin/env python

import subprocess
from tabulate import tabulate


def print_ip_table(ips):
	'''
	Функция print_ip_table
	отображает таблицу доступных
	и недоступных IP-адресов.
	'''
	ipresult = {}
	reach = []
	unreach = []
	for ip in ips:
		reply = subprocess.run(['ping', '-c', '2', ip]) #Проверяет доступность ip
		if reply.returncode == 0:
			reach.append(ip)
		else:
			unreach.append(ip)

	ipresult['Reachable'] = reach
	ipresult['Unreachable'] = unreach

	print(tabulate(ipresult, headers='keys')) #Выдаёт таблицу


ips = ['8.8.8.8', '192.168.19.220', '10.1.1.7', '10.1.1.8', '1.1.1.1']
print_ip_table(ips)


