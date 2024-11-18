import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "QUIT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Set up the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
    print(f"[CONNECTED] Connected to {SERVER}")
except:
    print("[ERROR] Connection failed!")
    exit()

username = input("Enter your username: ")

def receive():
    """Continuously listens for incoming messages from the server."""
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            if message:
                #format print if ack, else just print like normal message received
                if(message == "Msg received"):
                    continue
                print(f"{message}")
        except:
            print("Safely Disconnecting")
            client.close()
            exit()
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

# Send the username to the server
send(username)

# Continuously send messages to the server
print("Type messages to send. Type 'QUIT' to disconnect.")
while True:
    msg = input()
    if msg == DISCONNECT_MESSAGE:
        break
    send(f"{username}: {msg}")

client.close()
