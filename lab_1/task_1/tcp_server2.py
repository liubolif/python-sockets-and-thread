import socket
from datetime import datetime
import time

address = ('localhost', 44444)
max_size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
print('Starting the SERVER at', datetime.now())

server.listen(5)
print('Server is waiting for connection...')


clientsocket, addr = server.accept()
print('Got a connection from client: {}'.format(addr))

received_data = clientsocket.recv(max_size)
print('\tAt: {} \n\tclient: {}\n\tsaid: {}\n'.format(datetime.now(), addr, received_data.decode('utf-8')))
time.sleep(5)
send_echo = clientsocket.sendall(received_data)
print(send_echo, len(received_data))
if send_echo == len(received_data):  # перевірка, чи всі дані були надіслані
    print("All data was sent to the client.")
else:
    print("Something went wrong during sending the massage to client")

clientsocket.close()
server.close()