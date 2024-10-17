import socket

# Connect to the server
host = 'nigelward.com'
port = 80

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    # Send HTTP GET request
    request = 'GET /index.html HTTP/1.1\r\nHost: {}\r\n\r\n'.format(host)
    s.sendall(request.encode())

    # Receive response
    response = b""
    while True:
        part = s.recv(4096)
        if not part:
            break
        response += part

# Extract the relevant bytes
bytes_1001_to_1011 = response[1000:1011]
bytes_2001_to_2011 = response[2000:2011]

print("Bytes 1001-1011:", bytes_1001_to_1011)
print("Bytes 2001-2011:", bytes_2001_to_2011)
