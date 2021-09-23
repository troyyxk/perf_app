import socket
import sys
from typing import Protocol

if len(sys.argv) != 2:
    print("Require a port number, 1 command line arguement2")
    exit(1)

my_port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", my_port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    # CSP phase
    CSP_message = clientsocket.recv(1024)
    CSP_message = CSP_message.decode("utf-8")
    CSP_arguments = CSP_message.split(" ")
    if len(CSP_arguments) != 5:
        clientsocket.send(bytes("404 ERROR: Invalid Connection Setup Message"), "utf-8"))
        clientsocket.close()
        continue
    protocol_phase = CSP_arguments[0]
    measuremetn_type = CSP_arguments[1]
    number_of_probes = CSP_arguments[2]
    message_size = CSP_arguments[3]
    server_delay = CSP_arguments[4]
    if protocol_phase != 's' or \
        measuremetn_type not in ["rtt", "tput"] or \
            not number_of_probes.isnumeric() or \
                not measuremetn_type.isnumeric() or \
                    not server_delay.isnumeric():
        clientsocket.send(bytes("404 ERROR: Invalid Connection Setup Message"), "utf-8"))
        clientsocket.close()
        continue

    number_of_probes = int(number_of_probes)
    message_size = int(message_size)
    server_delay = int(server_delay)

    # TODO: Check piazza for restriction specifications



    clientsocket.send(bytes(CSP_message, "utf-8"))
    