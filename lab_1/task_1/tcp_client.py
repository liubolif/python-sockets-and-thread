import socket
from datetime import datetime

address = ('localhost', 44449)
max_size = 1024

print('Starting the CLIENT at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address)

print('Enter:\n\t\'q\' - to exit from client'
      '\n\t\'qq\' - to shut down the server and client as well')

while True:
    message = input("Enter massage: ").strip()
    client.sendall(message.encode('utf-8'))
    if message != 'q' and message != 'qq':
        received_data = client.recv(max_size)
        print('\tAt: {}\n\tsomeone replied: {}\n'.format(datetime.now(), received_data.decode('utf-8')))
    else:
        break
client.close()
