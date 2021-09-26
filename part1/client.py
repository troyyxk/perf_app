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

# connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((my_ip, my_port))

# send message
test_message = "A"
s.send(bytes(test_message, "utf-8"))

# receive message
return_mesage = s.recv(1024)
print(return_mesage.decode("utf-8"))
