# \n in python
# how to get the data size
import argparse
import socket
import sys
import datetime
# import matplotlib.pyplot as plt


# loop through the messsage to find the \n so the whole message is received
def loop_resv(s):
    received_message = ""
    while (True):
        cur_message = s.recv(1024).decode("utf-8")
        received_message += cur_message
        if '\n' in cur_message:
            break
    assert received_message[-1] == '\n'
    received_message = received_message.split('\n')[0]
    return received_message

# send number_of_probes of data with size message_size, there might be server_delay, return the rtt
def test_rtt( number_of_probes, message_size, server_delay):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((my_ip, my_port))

    time_durations = []
    # CSP phase
    CSP_message = "s rtt " + str(number_of_probes) + " " + str(message_size) + " " + str(server_delay) + "\n"
    s.send(bytes(CSP_message, "utf-8"))
    return_message = loop_resv(s)
    # TODO: delete testing prints
    print("In CSP phase")
    # print(return_message)
    # print(CSP_message)
    if return_message != "200 OK: Ready":
        return "error"

    # MP phase
    # TODO: delete testing prints
    print("In MT phase")
    for i in range(number_of_probes):
        # print("TODO: ", i)
        MP_message = "m " + str(i+1) + " " + ("1"*message_size) + "\n"
        a = datetime.datetime.now()
        s.send(bytes(MP_message, "utf-8"))
        return_message = loop_resv(s)
        b = datetime.datetime.now()
        time_durations.append((b-a).total_seconds())
        # print(return_message)


    # CTP phase
    print("In CTP phase")
    s.send(bytes("t\n", "utf-8"))
    return_message = loop_resv(s)
    # print(return_message)
    if return_message != "200 OK: Closing Connection":
        return "error"
    
    print("close connection with no error")
    s.close()

    return time_durations
    

if len(sys.argv) != 3:
    print("Require an ip address and a port number, 2 command line arguements")
    exit(1)

my_ip = sys.argv[1]
my_port = int(sys.argv[2])

# rtt in ms
my_server_delay = 0
rtt_1 = sum(test_rtt( 10, 1, my_server_delay))/10
rtt_100 = sum(test_rtt( 10, 100, my_server_delay))/10
rtt_200 = sum(test_rtt( 10, 200, my_server_delay))/10
rtt_400 = sum(test_rtt( 10, 400, my_server_delay))/10
rtt_800 = sum(test_rtt( 10, 800, my_server_delay))/10

latency_x = [1, 100, 200, 400, 800]
latency_y = [rtt_1, rtt_100, rtt_200, rtt_400, rtt_800]


rtt_1000 = sum(test_rtt( 10, 1000, my_server_delay))/10
rtt_2000 = sum(test_rtt( 10, 2000, my_server_delay))/10
rtt_4000 = sum(test_rtt( 10, 4000, my_server_delay))/10
rtt_8000 = sum(test_rtt( 10, 8000, my_server_delay))/10
rtt_16000 = sum(test_rtt( 10, 16000, my_server_delay))/10
rtt_32000 = sum(test_rtt( 10, 32000, my_server_delay))/10

throughput_x = [1000, 2000, 4000, 8000, 16000, 32000]
throughput_y = [1000/(rtt_1000/2),
 2000/(rtt_2000/2),
 4000/(rtt_4000/2),
 8000/(rtt_8000/2),
 16000/(rtt_16000/2),
 32000/(rtt_32000/2)]

print(latency_y)
print(throughput_y)