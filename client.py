# With Cursor AI


# Simple client that connects to the server, creates a Person protobuf message, serializes it, and sends it to the server.
import socket
import person_pb2   

def start_client(host='localhost', port=12345):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        # Create a Person message
        person = person_pb2.Person()
        person.user_name = "Alice"
        person.favourite_number = 42
        person.interests.extend(["reading", "hiking", "coding"])

        # Serialize the message to bytes
        serialized_data = person.SerializeToString()

        # Send the serialized data to the server
        client_socket.sendall(serialized_data)

        # Optionally, receive a response from the server (echoed data)
        response = client_socket.recv(1024)
        if response:
            print("Received echo from server.")
    finally:
        # Clean up the connection
        client_socket.close()


if __name__ == "__main__":
    start_client()