import socket
from datetime import datetime

address = ('localhost', 44445)
max_size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
print('Starting the SERVER at', datetime.now())

server.listen(5)
print('Server is waiting for connection...')


clientsocket, addr = server.accept()
print('Got a connection from client: {}'.format(addr))

received_data = clientsocket.recv(max_size)
print('At "{}" client "{}" said: "{}"'.format(datetime.now(), addr,  received_data.decode('utf-8')))

clientsocket.sendall('Dear client, are you talking to me?'.encode('utf-8'))

clientsocket.close()
server.close()




