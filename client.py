from socket import *

client = socket(AF_INET, SOCK_STREAM)  # create socket to connect
client.connect(('127.0.0.1', 8888))  # connect to server

client.send("Check".encode('UTF-8'))  # send + encode string to byte
client.close()