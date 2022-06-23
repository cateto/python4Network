from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

msg = '안녕, 난 client야.'
clientSock.send(msg.encode('utf-8'))

data = clientSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))