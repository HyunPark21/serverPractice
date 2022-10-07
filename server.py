# This is a project to learn server and socket in python
import socket
# import socket
from socket import *
import sys

# create socket of server
host = '127.0.0.1'
port = 8888
server = socket(AF_INET, SOCK_STREAM)  # create socket connecting internet, stream version

try:
    server.bind((host, port))  # use my ip address, port number = 8888
    server.listen(1)  # one can wait in line
    print('server start...')

    while True:
        conn, addr = server.accept()  # create another socket to communicate with client
        print('clinet add: ', addr)
        print(conn.recv(1024).decode('utf-8'))  # decode bye to string
except socket.error as err:
    print('Socket Error: ', err)
    sys.exit()
finally:
    server.close()

