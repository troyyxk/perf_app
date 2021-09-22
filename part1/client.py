import argparse
import socket

parser = argparse.ArgumentParser()

parser.add_argument("--ip", help="ip address", type=str, required=True)
parser.add_argument("--port", help="port number", type=int, required=True)
args = parser.parse_args()

my_ip = args.ip
my_port = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), my_port))

test_message = "Part 1 test message"

s.send(bytes(test_message, "utf-8"))

return_mesage = s.recv(1024)
print("Receive from server:")
print(return_mesage.decode("utf-8"))
