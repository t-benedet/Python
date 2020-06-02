#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler

# Configuration de la destination :

tftp_server = 'XXX.XXX.XXXX.XXX'
tftp_folder1 = 'XXX'
tftp_folder2 = 'XXX'
tftp_folder3 = 'XXX'
tftp_folder4= 'XXX'

filename_rubis = 'config-s1.bin'
filename_saphire = 'config-s2.bin'
filename_diamand = 'config-r1.bin'
filename_emeraude = 'config-r2.bin'


# Switchs Cisco

Rubis = {
    'device_type': 'cisco_ios',
    'ip': 'XXX.XXX.XXX.XXX',
    'username': 'XXX',
    'password': 'XXX',
    'secret': 'XXX',
    }

Saphire = { 'device_type': 'cisco_ios', 'ip': 'XXX.XXX.XXX', 'username': 'XXX', 'password': 'XXX', 'secret': 'XXX', }
Diamand = { 'device_type': 'cisco_ios', 'ip': 'XXX.XXX.XXX', 'username': 'XXX', 'password': 'XXX', 'secret': 'XXX', }
Emeraude = { 'device_type': 'cisco_ios', 'ip': 'XXX.XXX.XXX', 'username': 'XXX', 'password': 'XXX', 'secret': 'XXX', }


######################################### SWITCHS #############################################

# Rubis command

net_connect = ConnectHandler(**Rubis)
net_connect.enable()

cmd = 'copy start tftp://'+tftp_server+'/'+tftp_folder1+'/'+tftp_folder2+'/'+tftp_folder3+'/'+filename_rubis

output = net_connect.send_command(
    cmd,
    expect_string=r'Address or name of remote host [XXX.XXX.XXX]?'
    )

output += net_connect.send_command('\n', expect_string=r'Destination filename [IOS/Save/Switch/config-s1.bin]?')
output += net_connect.send_command('\n', expect_string=r'#')

print("")
print("Sauvegarde Rubis...")
print(output)
print("")

net_connect.exit_enable_mode()


## Saphire command

net_connect = ConnectHandler(**Saphire)
net_connect.enable()

cmd = 'copy start tftp://'+tftp_server+'/'+tftp_folder1+'/'+tftp_folder2+'/'+tftp_folder3+'/'+filename_saphire

output = net_connect.send_command(
            cmd,
            expect_string=r'Address or name of remote host [XXX.XXX.XXX]?'
            )

output += net_connect.send_command('\n', expect_string=r'Destination filename [IOS/Save/Switch/config-s2.bin]?')
output += net_connect.send_command('\n', expect_string=r'#')

print("Sauvegarde Saphire...")
print(output)
print("")

net_connect.exit_enable_mode()


########################################## ROUTERS #############################################

## Diamand command

net_connect = ConnectHandler(**Diamand)
net_connect.enable()

cmd = 'copy start tftp://'+tftp_server+'/'+tftp_folder1+'/'+tftp_folder2+'/'+tftp_folder4+'/'+filename_diamand

output = net_connect.send_command(
            cmd,
            expect_string=r'Address or name of remote host [XXX.XXX.XXX]?'
            )

output += net_connect.send_command('\n', expect_string=r'Destination filename [IOS/Save/Router/config-r1.bin]?')
output += net_connect.send_command('\n', expect_string=r'#')

print("Sauvegarde Diamand..." )
print(output)
print("")

net_connect.exit_enable_mode()


## Emeraude command

net_connect = ConnectHandler(**Emeraude)
net_connect.enable()

cmd = 'copy start tftp://'+tftp_server+'/'+tftp_folder1+'/'+tftp_folder2+'/'+tftp_folder4+'/'+filename_emeraude

output = net_connect.send_command(
            cmd,
            expect_string=r'Address or name of remote host [XXX.XXX.XXX]?'
            )

output += net_connect.send_command('\n', expect_string=r'Destination filename [TEST/SAVE/config-r2.bin]?')
output += net_connect.send_command('\n', expect_string=r'#')

print("Sauvegarde Emeraude..." )
print(output)
print("")

net_connect.exit_enable_mode()
