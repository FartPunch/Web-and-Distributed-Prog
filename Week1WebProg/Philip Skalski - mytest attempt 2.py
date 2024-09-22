import socket

def send_text_to_server(text):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    host = '127.0.0.1'
    port = 8081

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Send the text message
        client_socket.sendall(text.encode('utf-8'))

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    text = '{"firstName":"John", "lastname":"Smith"}'
    send_text_to_server(text)
