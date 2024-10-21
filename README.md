# Socket-Programming-Assignment
Implements a simple client-server communication application using TCP sockets in Python. The server handles multiple clients (Max. 3) and maintains a cache of the connected clients, when they were connected and disconnected at, their address, and their connection times.
Clients can send messages, ask for the status of the connected clients, and exit the session.

Features:
- Program can create a Server and 
- Each client created is assigned a name with correct number
- Server can handle multiple clients
- Server limits the number of connected clients to 3 clients at a time
- Server and client can exchange messages as described
- A client can send “exit” and server cleanly disconnects the client for new clients
- Server maintains clients’ connections details – sent to the client when client sends the status message to the server

