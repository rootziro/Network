# Tcp Server is essentially a listener that listens for incoming connections from clients.
# In addition, it's useful for when crafting a proxy or commnd shells.

import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')