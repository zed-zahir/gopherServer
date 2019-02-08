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
        try:
            fileToOpen = dataRequest[1]
        except IndexError:
            connection.send( "you didn't specify a file to open\n".encode() )
            print( "the peer didn't specify a file to open" )
            continue
        fileToOpen = dataRequest[ 1 ]
        try:
            f = open( fileToOpen.decode() )
        except:
            fileNotFound = "file: \"" + fileToOpen.decode() + "\" not found\n"
            connection.send( fileNotFound.encode() )
            print( "file the peer try access \"" + fileToOpen.decode() +"\" doesn't exist" )
            continue
        fRead = f.readlines()
        fRead = ''.join( fRead )
        fRead = fRead + '\n'
        connection.send( fRead.encode() )
    elif item.decode() == "1":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "2":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "3":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "4":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "5":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "6":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "7":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "8":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    elif item.decode() == "9":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    else:
        connection.send( "the protocol is broken, try 0 <file>\n".encode() )
        print( "the protocol is broken" )

s.close()

