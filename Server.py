import socket

s=socket.socket()
print("Socket created")
s.bind(('localhost',9999))
s.listen(2)
print("Waiting for connection")

while True:
    c,addr=s.accept()
    print(f"Got connection from {addr}")

    while True:
        msg=input("Server => ")
        c.send(msg.encode())

        if msg.lower()=='bye':
            break

        data=c.recv(1024).decode()
        print(f"Client: {data}")
        
        if data.lower()=='bye':
            break

    c.close
    break