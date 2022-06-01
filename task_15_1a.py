import re
regex1 = r'ip address (?P<ip>\S+) (?P<mask>\S+)'
regex2 = r'interface (?P<interface>\S+)'
result = {}
def get_ip_from_cfg2(config):
    with open(config, 'r') as f:
        for line in f:
            match = re.search(regex1, line)
            if 'interface' in line:
                interface = re.search(regex2, line).group(1)
            if match:
                result[interface] = match.groups()
    return result

print(get_ip_from_cfg2('config_r1.txt'))