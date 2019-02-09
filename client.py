#!/usr/bin/python3

import socket
import os
import sys
import time


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect( ( sys.argv[ 1 ], int( sys.argv[2] ) ) )
print( s.recv( 1024 ).decode() )
time.sleep( 3 )
if sys.argv[ 3 ] == "text":
    message = "0 " + sys.argv[ 4 ] + "\n"
    s.send( message.encode() )
    receivedInformations = s.recv( 1024 )
    print( receivedInformations.decode() )
