#!/usr/bin/python3

import socket
import os

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ( "127.0.0.1", 70 )
s.listen( 1 )
while True:
    connection, client = s.accept()
    request = connection.recv( 1024 )
    print( "request from: " + client[0] + " was " + request.decode() )
    dataRequest = request.split()
    print( dataRequest )
    item = dataRequest[ 0 ]
    if item.decode() == "0":
        f = open( dataRequest[ 1 ].decode() )
        fRead = f.readlines()
        connection.send( ''.join(fRead).encode() )
s.close()
