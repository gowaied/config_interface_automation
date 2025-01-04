# config_interface_automation

Network Device Configuration Automation Tool using Python and Netmiko

This Python script automates the configuration of interfaces on Cisco devices using the Netmiko library. It allows you to configure multiple interfaces with different IP addresses and subnet masks on multiple devices. The tool handles input validation, duplicate prevention, and error handling, streamlining the process of configuring network devices.
Features

    Automated Interface Configuration: Automatically configure multiple interfaces with IP addresses and subnet masks on multiple devices.
    Input Validation: Ensures proper IP address and subnet mask formatting and prevents duplicate IPs.
    VLAN Name Handling: Interface names and IPs are validated, and VLAN names can optionally be assigned.
    Error Handling: Prevents configuration errors related to invalid IPs or duplicate entries, and handles connection errors gracefully.
    Secure Input: Uses getpass to ensure secure credential input.

Requirements

    Python 3.x
    Netmiko library: Used for SSH connections and device automation.

Installation

To use this tool, you must install the required dependencies.
Install Required Libraries

pip3 install netmiko

How It Works

    Enter Device Credentials: Provide the necessary username, password, and enable secret for each device.
    Enter Device IPs: Input the IP addresses of the devices you want to configure. The tool supports configuring multiple devices simultaneously.
    Enter Interface Details: For each device, specify interface names, IP addresses, and subnet masks. Duplicate IPs and names are prevented.
    Validation and Configuration: The script validates the entered data and applies the configuration to each device, displaying output for each configuration step.

Usage

Run the script using the command:

python interface_automation.py

Example Output:

Please enter the number of devices as a numerical value: 1
*****************
Enter device 1's IP: 192.168.1.1
Enter this device username: admin
Please enter this device password: ********
Please enter this device secret: ********
Enter interface names one by one and type "done" when finish.
Enter name: GigabitEthernet0/1
Enter name: GigabitEthernet0/2
done
Please enter interface IPs one by one and type "done" when finish.
Enter interface IP: 192.168.1.10
Enter interface IP: 192.168.1.11
done
Please enter subnet masks one by one and type "done" when finish.
Enter Mask: 255.255.255.0
Enter Mask: 255.255.0.0
done
Connecting to host 192.168.1.1....
Configuring interfaces...
Interfaces have been configured successfully!

Error Handling

    Invalid IP Address: The script catches invalid IP addresses during input and prompts you to correct them.
    Duplicate Interface Names or IPs: The tool checks for duplicate interface names and IPs and ensures they are unique before proceeding.
    Connection Errors: The script gracefully handles authentication and timeout errors using Netmiko exceptions, ensuring reliable operation across multiple devices.

Known Issues

    Devices must have SSH access enabled for the script to connect successfully.
    The script has been tested primarily on Cisco IOS devices and may not be compatible with devices from other vendors.

Author

Mohamed Gowaied
- LinkedIn: [Mohamed Gowaied](https://www.linkedin.com/in/mohamed-gowaied/)
- GitHub: [Mohamed Gowaied](https://github.com/gowaied)
