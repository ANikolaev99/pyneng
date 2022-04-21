#!/usr/bin/env python


from pprint import pprint
from task_11_1 import parse_cdp_neighbors

infile = ("sh_cdp_n_sw1.txt",
            "sh_cdp_n_r1.txt",
                "sh_cdp_n_r2.txt",
                    "sh_cdp_n_r3.txt")


def create_network_map(filenames):
    '''
    Cкрипт, который будет обрабатывать конфигурационный файл config_sw1.txt.
    мя файла передается как аргумент скрипту.
    '''
    network={}
    for num in filenames:
        with open(num, "r") as f:
            #pprint(parse_cdp_neighbors(f.read()))
            network.update(parse_cdp_neighbors(f.read()))
    return network


if __name__ == "__main__":
    result = create_network_map(infile)
    pprint(result)
