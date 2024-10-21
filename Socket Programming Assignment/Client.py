#By Keenan Hannes ID: 169039829 and Ethan Katsiroubas ID:169036218
import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates socket object
    #AF_INET used for IPv4 address, SOCK_STREAM used for TCP connection
    client_socket.connect(('localhost', 12345)) #Connect to server

    while True:
        message = input("Enter message to send (type 'exit' to disconnect):") #enter string into message var
        client_socket.send(message.encode()) #sends message to the server
        if message == "exit":
            print("Session Ending")
            break #if message == exit then it breaks the loop and closes the socket, thus disconnecting from server
        

        data = client_socket.recv(1024).decode()
        print(f"Recieved from server: {data}")
        
    
    client_socket.close()

if __name__ == "__main__":
    client()