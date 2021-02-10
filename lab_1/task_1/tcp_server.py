import socket
from datetime import datetime
import time

address = ('localhost', 44442)
max_size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
print('Starting the SERVER at', datetime.now())

server.listen(5)
print('Server is waiting for connection...')

# тепер сервер здатен зчитувати інформацію не лише від одного клієнта
# сервер отримує підключення від клієнта, слухає його, а опісля готовий до підключення наступного клієнту
while True:
    clientsocket, addr = server.accept()
    print('Got a connection from client: {}'.format(addr))
    received_data = clientsocket.recv(max_size)

    # якщо клієнт ввів ключовий символ 'q' - відбувається закриття з'єднання з клієнтом
    if received_data.decode('utf-8') == 'q':
        print('Quitting from the server')
        break

    time.sleep(1)
    print('\tAt: {} \n\tclient: {}\n\tsaid: {}\n'.format(datetime.now(), addr, received_data.decode('utf-8')))

    clientsocket.sendall('Dear client, are you talking to me?'.encode('utf-8'))

server.close()
