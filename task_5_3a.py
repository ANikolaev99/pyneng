#!/usr/bin/env python

spi = input('Введите режим работы интерфейса (access/trunk): ')
eth = input('Введите тип и номер интерфейса: ')
qust = {'access':'Введите номер VLAN: ',
		'trunk':'Введите разрешенные VLANы: '}
vlan = input(qust[spi])

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]



access = '''
        interface {:<15}
        {:<15}
        {:<15}
        {:<15}
        {:<15}
        {:<15}
'''

trunk = '''
        interface {:<15}
        {:<15}
        {:<15}
        {:<15}
'''

temp = {'access': access.format(eth,
                                        access_template[0],
                                        access_template[1].replace('{}', vlan),
                                        access_template[2],
                                        access_template[3],
                                        access_template[4]),
                'trunk': trunk.format(eth,
                                        trunk_template[0],
                                        trunk_template[1],
                                        trunk_template[2].replace('{}', vlan))}

print('\n' + '-' * 30)

print(temp[spi])
