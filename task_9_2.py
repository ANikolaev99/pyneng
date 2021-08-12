#!/usr/bin/env python
generate_trunk = []

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    Задача 9_2 Функции
    '''
    for intrf in intf_vlan_mapping:
        generate_trunk.append('inteface {}'.format(intrf))
        generate_trunk.append(trunk_template[0])
        generate_trunk.append(trunk_template[1])
        generate_trunk.append(trunk_template[2] + ' ' + ','.join(str(e) for e in intf_vlan_mapping[intrf]))
    return print(generate_trunk)

generate_trunk_config(trunk_config, trunk_mode_template)


