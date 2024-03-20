import socket 

s=socket.socket()
s.connect(('localhost',9999))

while True:
    text=s.recv(1024).decode()
    print(f"Server: {text}")

    if text == 'bye':
        break

    msg=input("client => ")
    s.send(msg.encode())

    if msg.lower()=='bye':
        break

s.close