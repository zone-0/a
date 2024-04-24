import socket
import threading

# Server configuration
host = "127.0.0.1"
port = 65432

# List to keep track of clients (nodes)
clients = []
client_lock = threading.Lock()


def client_handler(conn, addr):
    global clients
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode("utf-8")
        if message == "REQUEST_TOKEN":
            with client_lock:
                current_index = clients.index(conn)
                next_index = (current_index + 1) % len(clients)
                clients[next_index].sendall(b"TOKEN")
    conn.close()
    with client_lock:
        clients.remove(conn)
    print(f"Disconnected {addr}")


def main():
    global clients
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with client_lock:
                clients.append(conn)
            threading.Thread(target=client_handler, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
