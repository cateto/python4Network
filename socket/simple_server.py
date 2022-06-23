from socket import *

# address family : 주소 체계 ex) AF_INET : IPv4
# socket type : 소켓 타입 ex) SOCK_STREAM 
serverSock = socket(AF_INET, SOCK_STREAM)

# ip, port 로 이루어진 어드레스 패밀리 -- 튜플 형식이어야 함
serverSock.bind(('', 8080))

# 동시접속가능자 수
serverSock.listen(1)

# 상대방 접속이 올때까지 대기하다가 수락
connectionSocket, addr = serverSock.accept()

print(f'connected : {connectionSocket} , address : {addr}')

