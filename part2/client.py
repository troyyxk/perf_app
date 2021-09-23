import argparse
import socket
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument("--ip", help="ip address", type=str, required=True)
# parser.add_argument("--port", help="port number", type=int, required=True)
# args = parser.parse_args()

if len(sys.argv) != 3:
    print("Require an ip address and a port number, 2 command line arguements")
    exit(1)

my_ip = sys.argv[1]
my_port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((my_ip, my_port))

test_message = "Part 1 test message"

s.send(bytes(test_message, "utf-8"))

return_mesage = s.recv(1024)
print(return_mesage.decode("utf-8"))
