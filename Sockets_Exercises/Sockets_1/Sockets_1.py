import socket

def main():
    host = '127.0.0.1'
    port = 7069

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        
        # Read two strings from the server
        for _ in range(2):
            data = s.recv(1024)  # Adjust buffer size if necessary
            if not data:
                break
            print(data.decode('utf-8').strip())

if __name__ == '__main__':
    main()
