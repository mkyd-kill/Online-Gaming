import pickle
import socket
from _thread import start_new_thread
from game import Game

server = socket.gethostbyname(socket.gethostname())
port = 5555
run = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

connected = set()
games = {} # game dictionary
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while run:
        try:
            data = conn.recv(2096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()

                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))

            else:
                break

        except:
            break

    
    print("Lost connection")
    try:
        del games[gameId]
        print("Closing game", gameId)

    except:
        pass
    
    idCount -= 1
    conn.close()

while run:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2

    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game.....")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))