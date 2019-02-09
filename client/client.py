#!/usr/bin/python3

import socket
import os
import sys
import time
from binascii import unhexlify

# check the parameters

if len( sys.argv ) != 5:
    print( "usage: script <ip address> <tcp port> <command> <the file>" )

# create the socket and connect

else: 
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.connect( ( sys.argv[ 1 ], int( sys.argv[2] ) ) )

    # print the text file read from the network steam

    print( s.recv( 1024 ).decode() )
    
    # send the parameter of 0 means "text"
    
    if sys.argv[ 3 ] == "text":
        message = "0 " + sys.argv[ 4 ]
        s.send( message.encode() )
        print(s.recv( 1024 ).decode())
        s.close()

    # send the parameter 5 emans "dos"

    elif sys.argv[ 3 ] == "dos":
        message = "5 " + sys.argv[ 4 ]
        s.send( message.encode() )
        receivedMessage =  s.recv( 1024 ).decode()
        print( receivedMessage )
        
        # check the condition if the user want to download the file
        
        if "the file exist" in receivedMessage:
            answerDownload = input(  )
            if "yes" in answerDownload:
                s.send( "yes".encode() )

                # open an empty file writable

                f = open( sys.argv[ 4 ], "wb" )
                print( "writing..." )

                # recv the data decode it unhexfy it then write it to the f socket

                f.write( unhexlify(s.recv( 5000 ).decode()) )
                print( "done!" )
                f.close()
            else:
                s.send( "no".encode() )
        s.close()

    # send the parameter 9 means "binary"

    elif sys.argv[ 3 ] == "binary":
        message = "9 " + sys.argv[ 4 ]
        s.send( message.encode() )
        receivedMessage = s.recv( 1024 ).decode()
        if "the file exist" in receivedMessage:
            print( "the file " + sys.argv[ 4 ] + " exist" )

            # open the file in binary and writable mode

            f = open( sys.argv[ 4 ], "wb" )
            print( "writing..." )

            # recv and decode and unhexify then write the data to the f socket

            f.write( unhexlify( s.recv( 5000 ).decode() ) )
            print( "done!" )
            f.close()
        else:
            s.close()
    else:
        print( "no parameter are specified" )
