import socket
import json

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = '127.0.0.1'
    port = 8081

    # Bind to the port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")
        # The server has received a first name of $firstName and a last name of $lastName".
        # Note that $firstName and %lastName
        json_data = json.loads(data)
        print(json_data["firstName"])
        # Close the connection
        client_socket.close()


if __name__ == "__main__":
    start_server()
