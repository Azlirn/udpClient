# Basic UDP Client
# Written by Azlirn

import socket

target_host = raw_input("Enter the target host (ONLY TESTED WITH IPv4 Addresses): ")
target_port = raw_input("Enter the target port: ")

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto("AAABBBCCC", (target_host, int(target_port)))

# Receive some data
data, addr = client.recvfrom(4096)

print data

exit()
