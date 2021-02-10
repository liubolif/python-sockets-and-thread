import socket
from datetime import datetime
import time

address = ('localhost', 44449)
max_size = 1024


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(address)
print('Starting the SERVER at', datetime.now())

server.listen(5)
print('Server is waiting for connection...')


# тепер сервер здатен зчитувати інформацію не лише від одного клієнта
# сервер отримує підключення від клієнта, слухає його, а опісля готовий до підключення наступного клієнту

class CloseServer(Exception): pass


try:
    while True:
        clientsocket, addr = server.accept()
        print('Got a connection from client: {}'.format(addr))
        while True:

            received_data = clientsocket.recv(max_size)
            # якщо клієнт ввів 'qq' - відбувається закриття з'єднання з клієнтом
            if received_data.decode('utf-8') == 'qq':
                print('Quitting from the server')
                raise CloseServer
            # якщо клієнт відімкнувся то виходмо із циклу обробки сповіщень від нього та готуємось до прослуховування нового клієнта
            elif received_data.decode('utf-8') == 'q':
                print('Client was disconnected from client'.format(addr))
                break
            time.sleep(1)
            print('\tAt: {} \n\tclient: {}\n\tsaid: {}\n'.format(datetime.now(), addr, received_data.decode('utf-8')))

            clientsocket.sendall('Dear client, are you talking to me?'.encode('utf-8'))
except CloseServer:
    server.close()
