import re
regex = r'ip address (?P<ip>\S+) (?P<mask>\S+)'
result=[]

def get_ip_from_cfg(config):
    with open(config, 'r') as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.groups())
    return result


print(get_ip_from_cfg('config_r1.txt'))
