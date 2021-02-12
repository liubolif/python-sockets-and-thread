# пробував робит завдання №5 за прикладом із сайту
# https://www.studytonight.com/network-programming-in-python/blocking-and-nonblocking-socket-io
import socket
from datetime import datetime

address = ('localhost', 44444)
max_size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
# якщо ставити тут - вибиває помилку
# server.setblocking(False)

print('Starting the SERVER at', datetime.now())

server.listen(5)
print('Server is waiting for connection...')


while True:
    clientsocket, addr = server.accept()
    print('Got a connection from client: {}'.format(addr))

    # якщо ставити тут - вибиває помилку
    # clientsocket.setblocking(False)
    received_data = clientsocket.recv(max_size)
    print("\t {}\n".format(received_data.decode('utf-8')))
    while received_data:
        print("\t {}\n".format(received_data.decode('utf-8')))
        received_data = clientsocket.recv(max_size)

    print("All data received")
    clientsocket.close()
    break

server.close()
