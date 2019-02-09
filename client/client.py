#!/usr/bin/python3

import socket
import os
import sys
import time


s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.connect( ( sys.argv[ 1 ], int( sys.argv[2] ) ) )
print( s.recv( 1024 ).decode() )
if sys.argv[ 3 ] == "text":
    message = "0 " + sys.argv[ 4 ]
    s.send( message.encode() )
    print(s.recv( 1024 ).decode())
    s.close()
elif sys.argv[ 3 ] == "dos":
    message = "5 " + sys.argv[ 4 ]
    s.send( message.encode() )
    receivedMessage =  s.recv( 1024 ).decode()
    print( receivedMessage )
    if "the file exist" in receivedMessage:
        answerDownload = input(  )
        if "yes" in answerDownload:
            s.send( "yes".encode() )
            f = open( sys.argv[ 4 ], "wb" )
            f.write( s.recv( 5000 ) )
            f.close()
        else:
            s.send( "no".encode() )
    s.close()
else:
    os.exit()
