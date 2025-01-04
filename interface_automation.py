from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
from getpass import getpass
import ipaddress

no_of_devices = int(input('Please enter the number of devices as a numerical value: '))


for device in range(no_of_devices):
        print('*****************')
        ip = input(f'Enter device {device + 1}\'s IP: ')
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            print('Error: Invalid IP address! Please try again')
        username = input('Please enter this device username: ')
        password = getpass('Please enter this device password: ')
        secret = getpass('Please enter this device secret: ')
        
        device = {
                'device_type' : 'cisco_ios',
                'host' : ip,
                'username' : username,
                'password' : password,
                'secret' : secret
             }
        

        #Gathering interfaces names
        int_name_list = []
        print('Enter interface names one by one and type "done" when finish.')
        while True:
            int_name = input('Enter name: ')
            if int_name.lower().strip() == 'done':
                break
            if int_name in int_name_list:
                print('Error: Interface name is already entered. Please enter another one.')
            else:
                int_name_list.append(int_name)
    
        #Gathering interface IPs
        int_ip_list = []
        print('Please enter interface IPs one by one and type "done" when finish.')
        while True:
            int_ip = input('Enter interface IP: ')
            if int_ip.lower().strip() == 'done':
                break
            try:
                ipaddress.IPv4Interface(int_ip)
            except ipaddress.AddressValueError:
                print('Error: Invalid IP address! Please try again.')
        
            if int_ip in int_ip_list:
                print('Error: Duplicate IP is detected. Please enter another one.')
            else:
                int_ip_list.append(int_ip)
            
        #Gathering Subnet masks
        subnetmask_list = []
        print('Please enter subnet masks one by one and type "done" when finish.')
        while True:
            subnetmask = input('Enter Mask: ')
            if subnetmask.lower().strip() == 'done':
                break
            try:
                ipaddress.IPv4Interface(subnetmask)
                subnetmask_list.append(subnetmask)
            except ipaddress.AddressValueError:
                print('Error: Invalid subnet mask! Please try again.')
        if len(int_ip_list) != len(int_name_list) or len(int_name_list) != len(subnetmask_list):
            print('Error: The number of interfaces IPs, subnet masks and names must be equal.')
            exit()

        try:
            for interface_name,interface_ip,interface_subnetmask, in zip(int_name_list, int_ip_list, subnetmask_list):
                print(f'Connecting to host {ip}....')
                net_connect = ConnectHandler(**device)
                net_connect.enable()
                commands = [f'int {interface_name}' , f'ip address {interface_ip} {interface_subnetmask}' , 'no shutdown']
                output = net_connect.send_config_set(commands)
                print(output)
                verification = net_connect.send_command('sh ip int br')
                print(verification)
                print('Interface have been configured successfully!')
        except NetMikoAuthenticationException:
            print(f'Error: Authentication failed for device {ip}! Please check credentials.')
        except NetMikoTimeoutException:
            print(f'Error: Timeout while connecting to device {ip}! This device might be unreachable.')  
    
print('All devices have been configured successfully!')
        