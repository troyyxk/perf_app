import argparse
import socket

parser = argparse.ArgumentParser()

parser.add_argument("--ip", help="ip address", type=str, required=True)
parser.add_argument("--port", help="port number", type=int, required=True)
args = parser.parse_args()

my_ip = args.ip
my_port = args.port

print("ip: ", my_ip)
print("port: ", my_port)
