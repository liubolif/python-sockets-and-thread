import socket
from datetime import datetime

address = ('localhost', 44445)
max_size = 1024

print('Starting the CLIENT at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address)

client.sendall('Hey!'.encode('utf-8'))
received_data = client.recv(max_size)

print('At "{}" someone replied : "{}"'.format(datetime.now(), received_data.decode('utf-8')))
client.close()
