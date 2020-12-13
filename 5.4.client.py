import socket
import sys
import os
import tqdm

SEPARATOR = '<SEPARATOR>'
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '172.20.10.13'
port = 8080

print(f'>> Connecting with {host}:{port}')
s.connect((host,port))
print('[+] Connected successfully!')

fname = input('[+]Enter name of file to be send: ')
print('Filename : ' , fname)

#filesize = os.path.getsize(filename)
#s.send(f'{filename}{SEPARATOR}{filesize}'.encode())

#progress = tqdm.tqdm(range(filesize, f'Sending {filename}', unit = 'B', unit_scale = True, unit_divisor = 1024)

file = open(fname, 'rb')
sendData = file.read(1024)
s.send(fname.encode('utf-8'))

while sendData:
        print(">> Received Message from server \n", s.recv(1024).decode('utf-8'))
        s.send(sendData)
        sendData = file.read(1024)

#with open(filename , 'rb') as f:
#       for _ in progress:
#               bytes_read = f.read(BUFFER_SIZE)
#               if not bytes_read:
#                       break

#               s.sendall(bytes_read)
#               progress.update(len(bytes_read))

s.close()
