# \n in python
# how to get the data size
import argparse
import socket
import sys
import datetime

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
    print(return_message)
    print(CSP_message)
    if return_message != "200 OK: Ready":
        return "error"

    # MP phase
    # TODO: delete testing prints
    print("In MT phase")
    for i in range(number_of_probes):
        print("TODO: ", i)
        MP_message = "m " + str(i+1) + " " + ("1"*message_size) + "\n"
        a = datetime.datetime.now()
        s.send(bytes(MP_message, "utf-8"))
        return_message = loop_resv(s)
        b = datetime.datetime.now()
        time_durations.append((b-a).total_seconds()*1000)
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
    




def test_tput( number_of_probes, message_size, server_delay):
    time_durations = []
    # CSP phase
    # MP phase
    # CTP phase

# parser = argparse.ArgumentParser()
# parser.add_argument("--ip", help="ip address", type=str, required=True)
# parser.add_argument("--port", help="port number", type=int, required=True)
# args = parser.parse_args()

if len(sys.argv) != 3:
    print("Require an ip address and a port number, 2 command line arguements")
    exit(1)

my_ip = sys.argv[1]
my_port = int(sys.argv[2])

# rtt in ms
rtt_1 = test_rtt( 10, 1, 0)
rtt_100 = test_rtt( 10, 100, 0)
rtt_200 = test_rtt( 10, 200, 0)
rtt_400 = test_rtt( 10, 400, 0)
rtt_800 = test_rtt( 10, 800, 0)

print (sum(rtt_1)/10)
print (sum(rtt_800)/10)
# print(rtt_800)
