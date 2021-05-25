#coding:utf-8
import socket

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost",15555))

file_name=input("Nom du fichier à demander au serveur:---->")
file_name=file_name.encode("utf8")
socket.sendall(file_name)
reponse=socket.recv(1024).decode("utf8")
while reponse:
    print(reponse)
    reponse=socket.recv(1024).decode("utf8")
