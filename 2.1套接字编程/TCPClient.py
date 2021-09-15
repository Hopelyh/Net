from socket import *
serverName = "10.0.197.32"
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())
modifiedSentence = clientSocket.recv(2048)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
