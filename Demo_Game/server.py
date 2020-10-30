# connection to a local server to host and run the game using sockets
# using sockets and threading to handle connections to the server

import socket
from _thread import *
import sys

server = "192.168.2.106"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # types of connections

# binding our port and server to the socket
try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen()  # this opens up the port for incoming and outgoing nodes
            # listen() takes one argument, leaving it blank gives the use of unlimited connections to happen
print("Waiting for a connection..., Server Started")


def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break

            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))

        except:
            break



while True:     # this continuesly check for connections
    conn, addr = s.accept() # this accepts any connection & stores the conn and address
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn))