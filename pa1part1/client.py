import argparse
import socket
import sys

# originally try to use flag but then realize simple command line argument would work
# but this works as well
# parser = argparse.ArgumentParser()
# parser.add_argument("--ip", help="ip address", type=str, required=True)
# parser.add_argument("--port", help="port number", type=int, required=True)
# args = parser.parse_args()

# check if has 2 command line argument
if len(sys.argv) != 3:
    print("Require an ip address and a port number, 2 command line arguements")
    exit(1)

# get the ip and port nubmer
my_ip = sys.argv[1]
my_port = int(sys.argv[2])

# if there are socket error, it will be catched
try:
    # connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((my_ip, my_port))

    # send message
    test_message = "A"
    s.send(bytes(test_message, "utf-8"))
    print("Message send: ", test_message)

    # receive message
    return_message = s.recv(1024)
    return_message = return_message.decode("utf-8")
    print("Message received: ", return_message)
except socket.error:
    print("Socket error")
    exit(1)
finally:
    s.close()