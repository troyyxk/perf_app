import socket

my_port = 58989

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), my_port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connetion from ", address, " has been accepted on port ", my_port)
    receive_message = clientsocket.recv(1024)
    receive_message = receive_message.decode("utf-8")
    clientsocket.send(bytes(receive_message, "utf-8"))

    s.close()
    exit()
