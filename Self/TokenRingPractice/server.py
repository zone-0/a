

import socket
import threading

clients = []
client_lock = threading.Lock()

host = "127.0.0.1"
port = 5555 

REQUEST_TOKEN = b"REQUEST_TOKEN"
TOKEN = b"TOKEN"

def client_handler(conn, add):
    global clients

    while True: 
        data = conn.recv(1024)
        if not data: break

        data = data.decode()
        if data == REQUEST_TOKEN:
            # This means it is done procssing ... ready to take change again ... but next time .
            with client_lock:
                next_conn = clients[(clients.index(conn) + 1 ) % len(clients)]
                next_conn.sendall(TOKEN)
    
    conn.close()
    with client_lock:
        clients.remove(conn)

    print("Disconnected")


def main():
    global clients
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()

        while True: 
            conn, add = s.accept()
            with client_lock: 
                clients.append(conn)
                if len(clients) == 1: 
                    conn.sendall(b"TOKEN")
            threading.Thread(
                target=client_handler,
                args=(conn,add)
            )


if __name__ == "__main__": 
    main()