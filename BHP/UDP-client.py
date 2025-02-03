import socket

# UDP is connectionless, so we don't need to establish a connection with the target. What we're looking for is to send packets to
# the target in UDP format.

target_host = "127.0.0.1"
target_port = 9997

# Establish connection
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AAABBBCCC", (target_host, target_port))

data, addr = client.recvfrom(4096)