#!/usr/bin/python3

import socket
import os
import sys
import time
from binascii import unhexlify

if len( sys.argv ) != 5:
    print( "usage: script <ip address> <tcp port> <command> <the file>" )
else:
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
                print( "writing..." )
                f.write( unhexlify(s.recv( 5000 ).decode()) )
                print( "done!" )
                f.close()
            else:
                s.send( "no".encode() )
        s.close()
    elif sys.argv[ 3 ] == "binary":
        message = "9 " + sys.argv[ 4 ]
        s.send( message.encode() )
        receivedMessage = s.recv( 1024 ).decode()
        if "the file exist" in receivedMessage:
            print( "the file " + sys.argv[ 4 ] + " exist" )
            f = open( sys.argv[ 4 ], "wb" )
            print( "writing..." )
            f.write( unhexlify( s.recv( 5000 ).decode() ) )
            print( "done!" )
            f.close()
        else:
            s.close()
    else:
        os.exit()
