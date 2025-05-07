import configparser
config = configparser.ConfigParser()

config.add_section('windows')

config.set('windows','windowsdesktop-1 general_settings','WindowsDesktop-1,4096\ Mb,2,/usr/bin/qemu-system-x86_64\ (v4.2.1),HDD,Send\ the\ shutdown\ signal\ (ACPI),vnc')
config.set('windows','windowsdesktop-1 network_settings','1,0c:4b:3c:0a:00:00,Intel\ Gigabit\ Ethernet\ (e1000),true')
config.set('windows','windowsdesktop-1 ansible_host','10.10.1.35')

config.set('windows','windowsdesktop-2 general_settings','WindowsDesktop-2,4096\ Mb,2,/usr/bin/qemu-system-x86_64\ (v4.2.1),HDD,Send\ the\ shutdown\ signal\ (ACPI),vnc')
config.set('windows','windowsdesktop-2 network_settings','1,0c:59:fd:86:00:00,Intel\ Gigabit\ Ethernet\ (e1000),true')
config.set('windows','windowsdesktop-2 ansible_host','10.10.1.36')

config.set('windows','windowsdesktop-3 general_settings','WindowsDesktop-3,4096\ Mb,2,/usr/bin/qemu-system-x86_64\ (v4.2.1),HDD,Send\ the\ shutdown\ signal\ (ACPI),vnc')
config.set('windows','windowsdesktop-3 network_settings','1,0c:e2:07:f3:00:00,Intel\ Gigabit\ Ethernet\ (e1000),true')
config.set('windows','windowsdesktop-3 ansible_host','10.10.1.43')

config.set('windows','windowsdesktop-4 general_settings','WindowsDesktop-4,4096\ Mb,2,/usr/bin/qemu-system-x86_64\ (v4.2.1),HDD,Send\ the\ shutdown\ signal\ (ACPI),vnc')
config.set('windows','windowsdesktop-4 network_settings','1,0c:46:74:35:00:00,Intel\ Gigabit\ Ethernet\ (e1000),true')
config.set('windows','windowsdesktop-4 ansible_host','10.10.1.29')

config.add_section('windows:vars')
config.set('windows:vars','ansible_user','Student')
config.set('windows:vars','ansible_password','P@ssw0rd')
config.set('windows:vars','ansible_connection','winrm')
config.set('windows:vars','ansible_winrm_transport','ntlm')
config.set('windows:vars','ansible_port','5985')

config.add_section('linux')

config.set('linux','test_box_1 general_settings','Test_Box_1,4096\ Mb,2,/usr/bin/qemu-system-x86_64\ (v4.2.1),HDD,Send\ the\ shutdown\ signal\ (ACPI),vnc')
config.set('linux','test_box_1 network_settings','1,0c:cb:a8:90:00:00,Intel\ Gigabit\ Ethernet\ (e1000),true')
config.set('linux','test_box_1 ansible_host','10.10.1.56')

config.set('linux','test_box_2 general_settings','Test_Box_2,4096\ Mb,2,/usr/bin/qemu-system-x86_64\ (v4.2.1),HDD,Send\ the\ shutdown\ signal\ (ACPI),vnc')
config.set('linux','test_box_2 network_settings','1,0c:50:a2:8a:00:00,Intel\ Gigabit\ Ethernet\ (e1000),true')
config.set('linux','test_box_2 ansible_host','10.10.1.57')

config.add_section('linux:vars')

config.set('linux:vars','ansible_user','student')
config.set('linux:vars','ansible_password','P@ssw0rd')
config.set('linux:vars','ansible_sudo_pass','P@ssw0rd')
config.set('linux:vars','ansible_connection','ssh')
config.set('linux:vars','ansible_ssh_extra_args','\'-o PreferredAuthentications=password -o PubkeyAuthentication=no\'')

config.add_section('switches')

config.set('switches','User_Network general_settings','User_Network,512Mb,1,/usr/bin/qemu-system-x86_64\ (v4.2.1),CD/DVD-ROM\ or\ HDD,Power\ off\ the\ VM,telnet')
config.set('switches','User_Network network_settings','13,0c:e0:f2:0b:00:00,Realtek\ 8139\ Ethernet\ (rtl8139),true')
config.set('switches','User_Network ansible_host','10.10.1.22')

config.set('switches','ACCT_Network general_settings','ACCT_Network,512Mb,1,/usr/bin/qemu-system-x86_64\ (v4.2.1),CD/DVD-ROM\ or\ HDD,Power\ off\ the\ VM,telnet')
config.set('switches','ACCT_Network network_settings','13,0c:40:34:07:00:00,Realtek\ 8139\ Ethernet\ (rtl8139),true')
config.set('switches','ACCT_Network ansible_host','10.10.1.32')

config.set('switches','MGMT_Network general_settings','MGMT_Network,512Mb,1,/usr/bin/qemu-system-x86_64\ (v4.2.1),CD/DVD-ROM\ or\ HDD,Power\ off\ the\ VM,telnet')
config.set('switches','MGMT_Network network_settings','13,0c:cc:78:5d:00:00,Realtek\ 8139\ Ethernet\ (rtl8139),true')
config.set('switches','MGMT_Network ansible_host','10.10.1.31')

config.set('switches','IT_Network general_settings','IT_Network,512Mb,1,/usr/bin/qemu-system-x86_64\ (v4.2.1),CD/DVD-ROM\ or\ HDD,Power\ off\ the\ VM,telnet')
config.set('switches','IT_Network network_settings','13,0c:1c:b2:85:00:00,Realtek\ 8139\ Ethernet\ (rtl8139),true')
config.set('switches','IT_Network ansible_host','10.10.1.30')

config.add_section('switches:vars')

config.set('switches:vars','ansible_user','ssh_user')
config.set('switches:vars','ansible_ssh_pass','P@ssw0rd')
config.set('switches:vars','ansible_connection','network_cli')
config.set('switches:vars','ansible_network_os','exos')

with open('inventory.ini','w') as f:
	config.write(f,space_around_delimiters=False)
