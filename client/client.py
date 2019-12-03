#!/usr/bin/python3

import socket
import os
import sys
import time
from binascii import unhexlify

# check the parameters

if len( sys.argv ) != 3:
    print( "usage: script <ip address> <tcp port>" )
    sys.exit()

# create the socket and connect

else: 
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.connect( ( sys.argv[ 1 ], int( sys.argv[2] ) ) )

    # print the text file read from the network steam

    print( s.recv( 1024 ).decode() )

    request = input()
    if int(request) > 3 and int(request) < 1:
        print( "there is an error while processing your request" )
        sys.exit()



    # send the parameter of 0 means "text"
    
    if int(request) == 1:
        data = input( "the text file name?" )
        message = "0 " + data
        s.send( message.encode() )
        print(s.recv( 1024 ).decode())
        s.close()

    # send the parameter 5 emans "dos"

    elif int(request) == 2:
        data = input( "the dos filename?" )
        message = "5 " + data
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

    elif int(request) == 3:
        data = input( "the binary filename?" )
        message = "9 " + data
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
