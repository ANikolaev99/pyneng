#!/usr/bin/env python

ip = input('Введите IP: ')

print('\n' + '-' * 30)
result = '''
Network:
{:<15}  {:<15}  {:<15}  {:<15}
{:<15}  {:<15}  {:<15}  {:<15}
Mask:
{:<15}
{:<15}  {:<15}  {:<15}  {:<15}
{:<15}  {:<15}  {:<15}  {:<15}
'''

#mask = {'/32': '255.255.255.255',
#        '/31': '255.255.255.254',
#        '/30': '255.255.255.252',
#        '/29': '255.255.255.248',
#        '/28': '255.255.255.240',
#        '/27': '255.255.255.224',
#        '/26': '255.255.255.192',
#        '/25': '255.255.255.128',
#        '/24': '255.255.255.0'}

print(result.format(
                        ip.split('.')[0],
                        ip.split('.')[1],
                        ip.split('.')[2],
                        #ip.split('.')[3].split('/')[0],
                        0,
                        bin(int(ip.split('.')[0])),
                        bin(int(ip.split('.')[1])),
                        bin(int(ip.split('.')[2])),
                        #bin(int(ip.split('.')[3].split('/')[0])),
                        bin(0),
                        '/24',
                        #mask[ip.split('.')[-1][1:]].split('.')[0],
                        #mask[ip.split('.')[-1][1:]].split('.')[1],
                        #mask[ip.split('.')[-1][1:]].split('.')[2],
                        #mask[ip.split('.')[-1][1:]].split('.')[3],
                        #bin(int(mask[ip.split('.')[-1][1:]].split('.')[0])),
                        #bin(int(mask[ip.split('.')[-1][1:]].split('.')[1])),
                        #bin(int(mask[ip.split('.')[-1][1:]].split('.')[2])),
                        #bin(int(mask[ip.split('.')[-1][1:]].split('.')[3]))))
			255,
			255,
			255,
			0,
			bin(255),
			bin(255),
			bin(255),
			bin(0)))

#print(result.format(bin(int(ip.split('.')[0])), ip.split('.')[1], ip.split('.')[2], ip.split('.')[3]))

