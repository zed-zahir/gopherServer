#!/usr/bin/python3

import socket
import os
import sys

print( """
        script as sgopher server
        usage: ./script.py <ip address> <tcp port>

        """)

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ( sys.argv[ 1 ], int( sys.argv[ 2 ] ) ) )
s.listen( 1 )
connection, client = s.accept()
connection.send( "=== Welcome to the Gopher server written in python by zahir meddour ===\n".encode())
while 1:
    request = connection.recv( 1024 )
    dataRequest = request.split()
    print( client, dataRequest )
    item = dataRequest[ 0 ]
    print( item )
    if item.decode() == "0":
        fileToOpen = dataRequest[ 1 ]
        try:
            f = open( fileToOpen.decode() )
        except:
            fileNotFound = "can't open the file: " + fileToOpen.decode() + '\n'
            connection.send( fileNotFound.encode() )
            continue
        fRead = f.readlines()
        fRead = ''.join( fRead )
        fRead = fRead + '\n'
        connection.send( fRead.encode() )
    else:
        connection.send( "the protocol is broken, try 0 <file>\n".encode() )
        print( "the protocol is broken" )

s.close()

