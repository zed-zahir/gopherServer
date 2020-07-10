#!/usr/bin/python3

import socket
import os
import sys
import time

# check the parameters

if len( sys.argv ) != 2:
    print( "usage: script <ip address>" )
    sys.exit()

# create the socket and connect

else:
    domain = sys.argv[1].split('/')[2]
    clientAddr = socket.gethostbyname(domain)
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.connect( ( clientAddr, 70 ) )

    # print the text file read from the network steam

    # print( s.recv( 1024 ).decode() )
    netParam = '/' + sys.argv[1].split('/')[4] + '\n'
    s.send(netParam.encode())

    print( s.recv( 1024 ).decode() )

