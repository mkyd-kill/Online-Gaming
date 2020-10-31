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
print("Waiting for a connection, Server Started")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0] + "," + tup[1])

pos = [(0,0), (100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break

            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:     # this continuesly check for connections
    conn, addr = s.accept() # this accepts any connection & stores the conn and address
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1