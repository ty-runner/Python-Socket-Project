import socket
import threading

# Constants for header size and port number
HEADER = 64
PORT = 5050

# Get the server's IP address and hostname
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
print(socket.gethostname())
ADDR = (SERVER, PORT)  # Create an address tuple for the server
FORMAT = 'UTF-8'  # Define the message format
DISCONNECT_MESSAGE = "!DISCONNECT"  # Message to disconnect the client

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)  # Bind the socket to the address and port

def handle_client(conn, addr):
    """Handles communication with a connected client."""
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True  # Track connection status
    while connected:
        # Receive the message length from the client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)  # Convert the length to an integer
            msg = conn.recv(msg_length).decode(FORMAT)  # Receive the actual message
            if msg == DISCONNECT_MESSAGE:  # Check for disconnect message
                connected = False  # Exit the loop if the client wants to disconnect
            print(f"[{addr}] {msg}")  # Print the received message
        conn.send("Msg received".encode(FORMAT))  # Acknowledge receipt of the message

    conn.close()  # Close the connection when done

def start():
    """Starts the server and listens for incoming connections."""
    server.listen()  # Start listening for incoming connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Accept a new connection
        conn, addr = server.accept()
        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()  # Start the thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Print active connections

print("[STARTING] server is starting...")
start()  # Start the server
