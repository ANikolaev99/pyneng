#!/usr/bin/env python

import ipaddress
ip_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

def convert_ranges_to_ip_list(ip_list):
    '''
    Функция convert_ranges_to_ip_list
    конвертирует список IP-адресов в разных форматах в список,
    где каждый IP-адрес указан отдельно.
    '''
    ip_reallist = []
    for ips in ip_list:
        if '-' in ips:
            start_ip, stop_ip = ips.split('-') #Определяет, есть-ли диапазон
            if '.' not in stop_ip:
                stop_ip = start_ip[:-1]+stop_ip
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for s in range(int(start_ip), int(stop_ip)+1):
                ip_reallist.append(str(ipaddress.ip_address(s))) #Цикл диапазона ip адресов 
        else:
            ip_reallist.append(ips)
    print(ip_reallist)

convert_ranges_to_ip_list(ip_list)


