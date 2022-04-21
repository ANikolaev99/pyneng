#!/usr/bin/env python

def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    r1 = {}
    for line in command_output.split("\n"):
        if '>' in line:
            host1 = line.split('>')[0]
        elif len(line.split()) > 2 and line.split()[3].isdigit():
            host2, interface1, interface2 = line.split()[0], line.split()[1]+line.split()[2], line.split()[-2]+line.split()[-1]
            r1.update({(host1, interface1): (host2, interface2)})
    return r1


if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))
