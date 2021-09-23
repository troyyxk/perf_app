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
    # MP phase
    CSP_message = clientsocket.recv(1024)
    CSP_message = CSP_message.decode("utf-8")
    CSP_arguments = CSP_message.split(" ")
    if len(CSP_arguments) != 5:
        clientsocket.send(bytes("404 ERROR: Invalid Connection Setup Message"), "utf-8")
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
        clientsocket.send(bytes("404 ERROR: Invalid Connection Setup Message"), "utf-8")
        clientsocket.close()
        continue

    # CSP success
    clientsocket.send(bytes("200 OK: Ready"), "utf-8")
    number_of_probes = int(number_of_probes)
    message_size = int(message_size)
    server_delay = int(server_delay)

    # TODO: Check piazza for restriction specifications

    # MP phase
    mp_has_error = False
    for i in range(number_of_probes):
        MP_message_raw = clientsocket.recv(100 + message_size)
        MP_message = MP_message_raw.decode("utf-8")
        MP_arguments = MP_message.split(" ")
        if len(MP_arguments) != 3:
            mp_has_error = True
            break
        protocol_phase = MP_arguments[0]
        probe_sequence_number = MP_arguments[1]
        payload = MP_arguments[2]
        if not probe_sequence_number.isnumeric():
            mp_has_error = True
            break
        probe_sequence_number = int(probe_sequence_number)
        if protocol_phase != 'm' or \
            probe_sequence_number != i + 1:
            mp_has_error = True
            break
        clientsocket.send(MP_message_raw)

    if mp_has_error:
        clientsocket.send(bytes("404 ERROR: Invalid Measurement Message"), "utf-8")
        clientsocket.close()
        continue

    # CTP phase
    CTP_message = clientsocket.recv(1024)
    CTP_message = CTP_message.decode("utf-8")
    protocol_phase = CTP_message[0]
    if protocol_phase != "t":
        clientsocket.send(bytes("404 ERROR: Invalid Connection Termination Message"), "utf-8")
    else:
        clientsocket.send(bytes("200 OK: Ready"), "utf-8")
    clientsocket.close()
    continue