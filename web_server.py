#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#SOCK_STREAM tells us that this is TCP
#Prepare a server socket
serverSocket.bind()	#serverSocket.bind(ip address, port number)
serverSocket.listen() #pick a small round number i guess
while True:
#Establish the connection
print('Ready to serve...')
connectionSocket, addr = serverSocket.accept() 
#Accept incoming requests to socket, checking the ip address as well as the port number

Try: 
message = connectionSocket.recv(1024) #Max Data size received #Fill in start #Fill in end
filename = message.split()[1]
f = open(filename[1:])
outputdata = f.read() #read the whole file of ‘f’
#Send one HTTP header line into socket
connectionSocket.send('HTTP/1.0 200 OK\r\n \r\n'.encode())
#Send the content of the requested file to the client
for i in range(0, len(outputdata)):
connectionSocket.send(outputdata[i].encode())
connectionSocket.send("\r\n".encode())
connectionSocket.close()
except IOError:
#Send response message for file not found
connectionSocket.send(“HTTP/ 1.1 404 Not Found\r\n”)#send 404 Not Found if file not found
#Fill in start
#Fill in end
#Close client socket
serverSocket.shutdown(SHUT_RDWR) 
#SHUT_RDWR means further sending and receiving is disallowed. Shutting down before closing is convention, as an advisory to the socket at the other end. 
serverSocket.close()
sys.exit()#Terminate the program after sending the correspon





#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = int(input("Input desired server port: "))
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Creates a connection socket from whatever address the server socket accepts
    try:
        message = connectionSocket.recv(1024).decode() #Decodes the message received from connection socket
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines() #Reads the contents of the file into a variable called outputdata
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP 1.1/200 OK\r\n'.encode()) #Sends encoded message saying request succeeded
        connectionSocket.send('\r\n'.encode()) #\r\n indicates end of header lines 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found'".encode()) #Sends encoded message saying 404 not found
        #Close client socket
        connectionSocket.close() #Closes the connection socket created earlier
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
