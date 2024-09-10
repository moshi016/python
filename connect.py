from netmiko import ConnectHandler

CSR = {
    "device_type": "cisco_ios",
    "ip": "devnetsandboxiosxe.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
}


net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('sh ip int br')
print(output)

net_connect.disconnect
