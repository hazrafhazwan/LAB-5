import socket


s = socket.socket()

port = 8888

s.connect(('172.20.10.13', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
