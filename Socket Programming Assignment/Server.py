import socket
import threading
from datetime import datetime

# By Ethan, 169036218 and Keenan, 169039829

# Variables
clientCache = {}
client_count = 0
max_clients = 3
clientID = 1
client_lock = threading.Lock()  # makes sure modifications to clientCache & client_count are properly used across multiple threads

def handle_client_cache(clientSocket, clientName, addr):
    global client_count

    connectionTime = datetime.now() # date formatted for the server
    with client_lock:
        clientCache[clientName] = {"address:": addr, "connected at:": connectionTime.strftime('%Y-%m-%d %H:%M:%S'), "disconnected at:": None}
    print(f"{clientName} connected from {addr} at {connectionTime}")

    try:
        while True:
            message = clientSocket.recv(1024).decode()  # 1024 is the max number of bytes to be recieved
            if not message:
                #clientCache[clientName]["disconnected at:"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # time client disconnected at
                #print(f"{clientName} has disconnected")
                break
            elif message == 'exit':
                break

            elif message == "status":
                status_message = "\n".join([f"{client}: {details}" for client, details in clientCache.items()])
                clientSocket.send(status_message.encode())  # The server sends cache to the client from status_message
                

            else:
                clientSocket.send(f"{message} ACK".encode())  # Sends message back with ACK at the end of message
                print(f"Message from {clientName}: {message}")

    finally:
        clientSocket.close()
        with client_lock:
            clientCache[clientName]["disconnected at:"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            client_count -= 1
        print(f"{clientName} disconnected. Current active clients: {client_count}")


def start_server():
    global client_count, clientID

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates tcp socket
    server_socket.bind(('localhost', 12345))  # Bind to localhost on port 12345
    server_socket.listen(6)  # max number of clients to accept
    print("Server is listening...")

    while True:
        # before accepting new connection, server checks if num of clients connected is less than 3, if it is then accepts connection
        client_socket, addr = server_socket.accept()
        with client_lock:
            if client_count < max_clients:
                #client_socket, addr = server_socket.accept()
                client_count += 1
                print(f"Connection from {addr}")
                client_name = f"Client{clientID:02}"
                clientID +=1

                client_thread = threading.Thread(target = handle_client_cache, args=(client_socket, client_name, addr))
                client_thread.start()
            else:
                print("The server is at max capacity")
                client_socket.send("Server is full. Please try again later.".encode())
                client_socket.close()

if __name__ == '__main__':
    start_server()
