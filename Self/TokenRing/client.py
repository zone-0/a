import socket
import time
import random

# Server configuration to connect to
host = "127.0.0.1"
port = 65432


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        # Initially request the token
        s.sendall(b"REQUEST_TOKEN")
        while True:
            data = s.recv(1024)
            if data == b"TOKEN":
                print("Received TOKEN. Entering critical section.")
                time.sleep(random.uniform(1, 3))  # Simulate work in critical section
                print("Exiting critical section.")
                # Inform server upon exiting critical section to pass the token
                s.sendall(b"REQUEST_TOKEN")


if __name__ == "__main__":
    main()
