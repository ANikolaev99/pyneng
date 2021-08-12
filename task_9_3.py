#!/usr/bin/env python

#access = {}
#trunk = {}

def get_int_vlan_map (config):
    access = {}
    trunk = {}
    with open(config) as f:
        for line in f:
            if 'FastEthernet' in line:
                interface = line.split()[-1]
            elif 'access vlan' in line:
                acess_vlan = line.split()[-1]
                access[interface] = acess_vlan
            elif 'trunk allowed' in line:
                trun_vlan = line.split()[-1]
                trunk[interface] = trun_vlan
    return print(access, trunk)
    
get_int_vlan_map('config_sw1.txt')

