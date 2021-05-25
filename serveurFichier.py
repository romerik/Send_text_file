#coding:utf-8
import socket
import threading

class ClientSocket(threading.Thread):
    def __init__(self,sockClient,ip,address):
        threading.Thread.__init__(self)
        self.sockClient=sockClient
        self.ip,self.address=(ip,address)
        print("Connecion by {} {}".format(self.ip,self.address))
    def run(self):
        fileAskByClentName=self.sockClient.recv(2048).decode("utf8")
        with open(fileAskByClentName,'r') as file:
            contenu=file.read()
        self.sockClient.sendall(contenu.encode("utf8"))
        print("Connection Terminée avec l'adresse ip {} connecté au port {}".format(self.ip,self.address))
        self.sockClient.close()

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("",15555))
print("......Listening.....")

while True:
    serverSocket.listen(10)
    newClient,(ip,address)=serverSocket.accept()
    newThread=ClientSocket(newClient,ip,address)
    newThread.start()