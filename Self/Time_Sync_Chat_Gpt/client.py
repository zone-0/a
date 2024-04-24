import random
import socket
import time
import json

def adjust_time(adjustment):
    """Adjust client's time (mocked) based on server's response."""
    print(f"Adjusting time by {adjustment} seconds.")

def main():
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # Send current time as bytes to server
        current_time = int(time.time()) + random.randint(-100,100)
        # print("current time :  " , current_time)
        s.sendall(json.dumps({"time": current_time}).encode())

        # Receive and apply adjustment
        adjustment_bytes = json.loads(s.recv(1024).decode())["adjustment"]
        adjustment =  adjustment_bytes
        adjust_time(adjustment)

if __name__ == "__main__":
    main()
