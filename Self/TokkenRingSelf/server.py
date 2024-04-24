from http import client
import threading
import socket

host = "127.0.0.1"
port = 5555

clients = [] 
client_lock = threading.Lock()


def clinet_handler(conn, addr):
    global clients
    print(f"Client connected : {conn} : {addr}")

    while True:
        data = conn.recv(1024)
        if not data: 
            break
        message = data.decode()
        if data == b"REQUEST_TOKEN" :
            with client_lock: 
                curr_index = clients.index(conn)
                next_index = (curr_index + 1 ) % len(clients)
                clients[next_index].sendall(b"TOKEN")

    conn.close()
    with client_lock: 
        clients.remove(conn)

    print("Client Disconnected")

def main():
    global clients
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()

        while True:
            conn , add = s.accept()
            with client_lock:
                clients.append(conn)
                if len(clients) == 1: 
                    conn.sendall(b"TOKEN")
            threading.Thread(
                target=clinet_handler,
                args=(conn,add)
            ).start()
            

if __name__ == "__main__":
    main()