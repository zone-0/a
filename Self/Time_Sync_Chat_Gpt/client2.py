import socket
import struct
import time

def adjust_time(adjustment):
    """Adjust the client's time (mocked) based on server's response."""
    # This is a mock function. In a real scenario, you would adjust the system's clock.
    print(f"Adjusting time by {adjustment} seconds")

def main():
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # Send current time to server
        current_time = time.time()
        s.sendall(struct.pack('d', current_time))

        # Initialize an empty bytes object for the adjustment data
        adjustment_data = b''
        # Keep receiving data until we have exactly 8 bytes
        while len(adjustment_data) < 8:
            more_data = s.recv(8 - len(adjustment_data))
            if not more_data:  # If no more data is received, break out of the loop
                break
            adjustment_data += more_data

        # Only attempt to unpack if we received exactly 8 bytes
        if len(adjustment_data) == 8:
            adjustment = struct.unpack('d', adjustment_data)[0]
            adjust_time(adjustment)
        else:
            print("Error: Did not receive the correct amount of adjustment data.")

if __name__ == "__main__":
    main()
