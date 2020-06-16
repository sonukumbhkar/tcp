import socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host =socket.gethostname()
port = 444
serversocket.bind((host,port))
serversocket.listen(3)
while True:
    clientsocket ,address = serversocket.accept()
    print("recieved connection from %s"%str(address))
    message = 'thankyou for connecting'+"\r\n"
    clientsocket.send(message.encode('asci'))
    clientsocket.close()
    
