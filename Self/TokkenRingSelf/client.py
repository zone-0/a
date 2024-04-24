import socket 
import time 

host = "127.0.0.1"
port = 5555


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        print("Connected to server ::  🚀")
        while True:
            data = s.recv(1024)
            if data == b"TOKEN":
                # Recived ......  ✅
                print("Recived token working !!!🛡️🛡️🛡️")
                time.sleep(2) 
                print("Done bc ... Released token✅✅✅")
                s.sendall(b"REQUEST_TOKEN")


if __name__ == "__main__":
    main()