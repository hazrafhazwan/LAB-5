import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'[+] Socket created')

port = 8080
s.bind(('', port))
print(f'[+] Socket successfully bind to ' + str(port))

s.listen(5)
print(f'>> Socket listening.. | Port: {port}')

while True:
	conn, addr = s.accept()
	print('>> Connection connect successfully!')

	fname = conn.recv(1024)
	file = open(fname, 'wb')

	msg = 'hi thank you for using this server'
	conn.send(msg.encode('utf=8'))

	recvData = conn.recv(1024)
	while recvData:
		file.write(recvData)
		recvData = conn.recv(1024)

	file.close()
	print('>> File has been received successfully!')

	conn.close()
	print('>> Server closing connection. Bye-bye \n')
	break

#client_socket, address = s.accept()

#print(f'[+] {address} is connected.')

#received = client_socket.recv(BUFFER_SIZE).decode()
#filename, filesize = received.split(SEPERATOR)

#filename = os.path.basename(filename)
#filesize = int(filesize)

#progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit = "B", unit_scale = True, unit_divisor = 1024)
#with open(filename, "wb") as f:
#        for _ in progress:
#                bytes_read = client_socket.recv(BUFFER_SIZE)
#                if not bytes_read:
#                        print("File has been received!")
#                        break

#                f.write(bytes_read)
#                progress.update(len(bytes_read))

#client_socket.close()
#s.close()
