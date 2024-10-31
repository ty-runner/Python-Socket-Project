import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Set up the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    """Continuously listens for incoming messages from the server."""
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            if message:
                print(f"[BROADCAST] {message}")
        except:
            # If an error occurs, break the loop and close the connection
            print("[ERROR] An error occurred!")
            client.close()
            break

def send(msg):
    """Sends a message to the server."""
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

# Start a thread to listen for broadcasted messages from the server
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Main loop to send messages to the server
print("Type messages to send. Type '!DISCONNECT' to disconnect.")
while True:
    msg = input()
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        break

client.close()
