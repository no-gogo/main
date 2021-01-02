import socket

print("Start.")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to http://data.pr4e.org/intro-short.txt' ")
mysock.connect(('data.pr4e.org', 80))
print("Sending command")
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

print('\n\n')

print("Receiving Data: \n")
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    try:
    	print(data.decode(), end='')
    except:
    	print("Wtf")

mysock.close()

#http://data.pr4e.org/intro-short.txt