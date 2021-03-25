#!/usr/bin/env python

ip = input('ВведитуIP-сети в формате 10.1.1.0/24: ')

print('\n' + '-' * 30)
result = '''
Network:
{:<15}	{:<15}	{:<15}	{:<15}
{:08b}	{:08b}	{:08b}	{:08b}
Mask:
{:<15}
{:<15}	{:<15}	{:<15}	{:<15}
{:08b}	{:08b}	{:08b}	{:08b}
'''

mask = {'/32': '255.255.255.255',
	'/31': '255.255.255.254',
	'/30': '255.255.255.252',
	'/29': '255.255.255.248',
	'/28': '255.255.255.240',
	'/27': '255.255.255.224',
	'/26': '255.255.255.192',
	'/25': '255.255.255.128',
	'/24': '255.255.255.0'}

print(result.format(
			ip.split('.')[0], 
			ip.split('.')[1], 
			ip.split('.')[2], 
			ip.split('.')[3].split('/')[0], 
			int(ip.split('.')[0]), 
			int(ip.split('.')[1]),
			int(ip.split('.')[2]),
			int(ip.split('.')[3].split('/')[0]),
			ip.split('.')[-1][1:],
			mask[ip.split('.')[-1][1:]].split('.')[0],
			mask[ip.split('.')[-1][1:]].split('.')[1],
			mask[ip.split('.')[-1][1:]].split('.')[2],
			mask[ip.split('.')[-1][1:]].split('.')[3],
			int(mask[ip.split('.')[-1][1:]].split('.')[0]),
			int(mask[ip.split('.')[-1][1:]].split('.')[1]),
			int(mask[ip.split('.')[-1][1:]].split('.')[2]),
			int(mask[ip.split('.')[-1][1:]].split('.')[3])))

#print(result.format(bin(int(ip.split('.')[0])), ip.split('.')[1], ip.split('.')[2], ip.split('.')[3]))

