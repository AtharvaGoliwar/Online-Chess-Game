import socket
import pickle

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        #self.server = "Enter the IPV4 address of the Server"   #Remove the comment to run the code and enter your IPV4 address in given strings
        self.port = 9090
        self.addr = (self.server,self.port)
        #self.p = self.connect()
        self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)              #This will connect the client to the respective server and port
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(data)                     #Sending data to the server
        except socket.error as e:
            print(e)

    def receive(self):
        data = self.client.recv(4096)                  #Receiving data from the server
        try:
            print("Receiving")
            self.recv_data = pickle.loads(data)        #Converting bytes data to readable data
            print(self.recv_data)
        except:
            self.recv_data = data.decode()
            print(self.recv_data)
        #print("broke successfully")
        return str(self.recv_data)


