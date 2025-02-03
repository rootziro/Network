import socket

target_host = '10.10.241.145'
target_port = 80

# Socket object. Used to establish a connection to the target, allowing us to send and receive data.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish a connection to the target
client.connect((target_host, target_port))

# Send some data. Essential for communication between the client and server.
client.send(b'GET / HTTP/1.1\r\nHost:10.10.241.145\r\n\r\n')

# Receive some data
response = client.recv(4096)

print(response.decode)
client.close()