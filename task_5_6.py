#!/usr/bin/env python

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
print (mac)
mac_cisco = []
for mc in mac:
	if ':' in mc:
		mac_cisco.append(mc.replace(':', '.'))
print(mac_cisco)

