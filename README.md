# Python-Socket-Project

You are tasked with creating a client-server chat application using Python's socket module. The application should allow multiple clients to connect to the server and exchange messages in real-time. The server should be able to relay messages between connected clients, and clients should be able to send messages to the server, which will broadcast them to all connected clients. Clients should also be able to disconnect from the server gracefully.

## 1. Server Implementation:
The server should listen for incoming connections from clients on a specified IP address and port.
Once a client connects, the server should store the client's information (e.g., IP address, port) and allow the client to send and receive messages.
The server should be able to handle multiple clients concurrently using threads or any other appropriate method.
The server should relay messages between clients, broadcasting messages from one client to all other connected clients.
## 2. Client Implementation:
The client should be able to connect to the server using the server's IP address and port.
Once connected, the client should be able to send messages to the server, which will broadcast them to all other connected clients.
The client should be able to receive messages from the server and display them on the screen.
The client should be able to gracefully disconnect from the server upon user request.
User Interface:
Implement a simple command-line interface for both the server and the client. For example, the user can type "CONNECT" to connect to the server, "SEND <message>" to send a message, and "QUIT" to disconnect from the server.
Display appropriate messages for successful connections, disconnections, and error conditions.
### Bonus Points (Optional):

Implement error handling for cases such as connection failures, disconnections, and invalid commands.
Add additional features, such as user authentication, private messaging between clients, or file transfer capabilities.
Implement a GUI (Graphical User Interface) for the client using a Python library such as tkinter or PyQt.
Submission: Submit a zip file containing the following:

1. Server-side Python code
2. Client-side Python code
3. A text file explaining the usage of the chat application, including instructions for running the server and client.
4. Any additional files or resources used in the implementation.
