import socket
from datetime import datetime

address = ('localhost', 44442)
max_size = 1024

print('Starting the CLIENT at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address)

message = input("Enter massage: ").strip()
client.sendall(message.encode('utf-8'))
if message != "q":
    received_data = client.recv(max_size)
    print('\tAt: {}\n\tsomeone replied: {}\n'.format(datetime.now(), received_data.decode('utf-8')))
client.close()
