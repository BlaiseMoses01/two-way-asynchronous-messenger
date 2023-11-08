# Written by Blaise Moses Copyright 2023

# Implementation of a two way message client

# Import socket related methods
from socket import *

# Import argv related methods
from sys import *
import time


# Client needs server's contact information
if len(argv) != 3:
    print("usage:", argv[0], "<server name> <server port>")
    exit()

# Get server's whereabouts
serverName = argv[1]
serverPort = int(argv[2])

# Create a socket
sock = socket(AF_INET, SOCK_STREAM)

# Connect to the server
sock.connect((serverName, serverPort))
print(f"Connected to server at ('{serverName}', '{serverPort}')");

# Make a file stream out of socket
sockFile = sock.makefile()

# Keep reading lines and send to server
while True:
    sock.send(stdin.readline().encode())

    # Read a message from the server
    message = sockFile.readline()

    # If no message ==> server closed the connection
    if not message:
        print('Server closed connection')
        sockFile.close()
        sock.close()
        break

    # Display the line
    print(serverName, ': ', message)

print("Closing connection")
sock.close()
