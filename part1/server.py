import socket
import sys

if len(sys.argv) != 2:
    print("Require a port number, 1 command line arguement2")
    exit(1)

my_port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", my_port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connetion from ", address, " has been accepted on port ", my_port)
    receive_message = clientsocket.recv(1024)
    receive_message = receive_message.decode("utf-8")
    clientsocket.send(bytes(receive_message, "utf-8"))
