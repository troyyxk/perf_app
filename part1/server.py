import socket
import sys

# check if it has 1 command line arguement
if len(sys.argv) != 2:
    print("Require a port number, 1 command line arguement2")
    exit(1)

# get the port number
my_port = int(sys.argv[1])

# start listerning
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", my_port))
s.listen(5)

# echo back received messages
while True:
    clientsocket, address = s.accept()
    receive_message = clientsocket.recv(1024)
    receive_message = receive_message.decode("utf-8")
    clientsocket.send(bytes(receive_message, "utf-8"))
    