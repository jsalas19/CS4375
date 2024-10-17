#!/usr/bin/env python3
from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 7069))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from" , a)
    c.send("miércoles\n".encode())
    time.sleep(0.5)
    c.send("Hello again\n".encode())
    c.close()


