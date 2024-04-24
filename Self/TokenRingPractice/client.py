

import socket

host = "127.0.0.1"
port = 5555 


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))

        while True: 
            data = s.recv(1024).decode()
            if data == b"TOKEN":
                s.sendall(b"REQUEST_TOKEN")

if __name__ == "__main__":
    main()