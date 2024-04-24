import socket
import json
import time

# Server configuration
host = "127.0.0.1"
port = 65432

def main():
    clients = []
    client_times = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server listening for connections...")

        # Accept connections
        while len(clients) < 3:  # Expecting 3 clients for simplicity
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            clients.append((conn, addr))

        # Receive times from clients
        for conn, addr in clients:
            data = conn.recv(1024).decode()
            client_time = json.loads(data)["time"]
            client_times.append((client_time, conn))

        # Calculate the target time (for simplicity, the average time)
        target_time = int(sum(client_time for client_time, _ in client_times) / len(client_times))
        
        # Send custom adjustment to each client
        for client_time, conn in client_times:
            adjustment = target_time - client_time
            adjustment_data = json.dumps({"adjustment": adjustment})
            conn.sendall(adjustment_data.encode())
            conn.close()

if __name__ == "__main__":
    main()
