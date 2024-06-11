import socket

def listen_for_key(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for incoming connections on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")

    key = conn.recv(1024)  # Adjust the buffer size as needed
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    conn.close()
    server_socket.close()
    print("Key has been received and saved.")

if __name__ == '__main__':
    listen_for_key()