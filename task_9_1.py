#!/usr/bin/env python
access_config_list = []
access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}
access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def generate_access_config(intf_vlan_mapping, access_template):
    for access in intf_vlan_mapping:
        access_config_list.append('inreface {} '.format(access))
        access_config_list.append(access_mode_template[0])
        access_config_list.append(access_mode_template[1]+' {}'.format(access_config[access]))
        access_config_list.append(access_mode_template[2])
        access_config_list.append(access_mode_template[2])
        access_config_list.append(access_mode_template[3])
        access_config_list.append(access_mode_template[4])
        return access_config_list
        

result = generate_access_config(access_config_2, access_mode_template)
print(result)

