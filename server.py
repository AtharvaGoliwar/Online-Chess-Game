import socket
from _thread import *
import pickle

server = socket.gethostbyname(socket.gethostname())
port= 9090
print(server)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((server,port))

s.listen()
print("Waiting for connections, Server Started")
clients = []

def threaded_client(conn):
    #from chess import chess
    if len(clients)!=2:
        conn.send(pickle.dumps(["Connected to the server",0]))
    print(len(clients))
    if len(clients)==2:
                    print("Bhej diya")
                    conn.send(pickle.dumps(["Start Game",1]))
                    clients[0][0].send("Start Game".encode())
    while True:
        try:
            data = conn.recv(2048)
            if not data:
                print("Disconnected")
                break
            else:
                #print(str(data).decode())     #Temporary command
                print(pickle.loads(data))
                for i in range(2):
                    if clients[i][0]!=conn:
                        print("Sending")
                        clients[i][0].send(data)
                        print("Sent")
        except:
            break

n=0
while True:
    conn,addr = s.accept()
    conn.send(str.encode(str(n)))
    clients.append((conn,n))
    print(clients)
    n+=1
    print("Connected to: ",addr)

    start_new_thread(threaded_client,(conn,))

