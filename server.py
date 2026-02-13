# With Cursor AI 

# Simple single-threaded server that listens for incoming connections and echoes back any received data.
# Reads the Person protobuf message from the client, deserializes it, and prints the contents.

import socket
import person_pb2   

def start_server(host='localhost', port=12345):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if data:
                # Deserialize the received data into a Person message
                person = person_pb2.Person()
                person.ParseFromString(data)

                # Print the contents of the Person message
                print(f"Received Person: user_name={person.user_name}, "
                      f"favourite_number={person.favourite_number}, "
                      f"interests={list(person.interests)}")

                # Echo the data back to the client
                client_socket.sendall(data)
        finally:
            # Clean up the connection
            client_socket.close()



if __name__ == "__main__":
    start_server()