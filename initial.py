import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
print(host)
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

while True:
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    # Send a message to the client
    message = 'Thank you for connecting'
    client_socket.send(message.encode('utf-8'))

    # Close the connection
    client_socket.close()