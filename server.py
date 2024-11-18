import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "QUIT"

# List to store connected clients and their usernames
clients = {}
lock = threading.Lock()

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def broadcast(message, sender_conn):
    """Sends a message to all clients except the sender."""
    for client in clients:
        if client != sender_conn:  # Skip the sender
            client.send(message.encode(FORMAT))

def handle_client(conn, addr):
    """Handles communication with a connected client."""
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    username_length = conn.recv(HEADER).decode(FORMAT)
    if username_length:
        username_length = int(username_length)
        username = conn.recv(username_length).decode(FORMAT)
        with lock:
            clients[conn] = username
    print(f"[USERNAME] {username} connected.")

    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    print(f"{username} disconnected.")
                    connected = False
                    break
                print(f"{msg}")
                broadcast(f"{msg}", conn)  # Broadcast to all except sender

            conn.send("Msg received".encode(FORMAT))
        except:
            print("A client disconnected.")
            break

    conn.close()
    with lock:
        del clients[conn]  # Remove the client from the list when disconnected

def start():
    """Starts the server and listens for incoming connections."""
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()
