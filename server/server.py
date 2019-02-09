#!/usr/bin/python3

import socket
import os
import sys
import time

if len( sys.argv ) < 3:
    print( "script as sgopher server\nusage: ./script.py <ip address> <tcp port>")
    sys.exit()
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ( sys.argv[ 1 ], int( sys.argv[ 2 ] ) ) )
s.listen( 1 )
while 1:
    connection, client = s.accept()
    time.sleep( 1 )
    connection.send( "=== Welcome to the Gopher server written in python by zahir meddour ===\n".encode())
    try:
        request = connection.recv( 1024 )
    except:
        print( "bad connection" )
    if request == None:
        continue
    dataRequest = request.split()
    print( client, dataRequest )
    try:
        item = dataRequest[ 0 ]
    except IndexError:
        connection.send( "internal error\n".encode() )
        print( "internal error" )
        break
    if item.decode() == "0":
        try:
            fileToOpen = dataRequest[1]
        except IndexError:
            connection.send( "you didn't specify a file to open\n".encode() )
            print( "[0] the peer didn't specify a file to open" )
            continue
        fileToOpen = dataRequest[ 1 ]
        try:
            f = open( "../Downloads/" + fileToOpen.decode() )
        except:
            fileNotFound = "file: \"" + fileToOpen.decode() + "\" not found\n"
            connection.send( fileNotFound.encode() )
            print( "file the peer try access \"" + fileToOpen.decode() +"\" doesn't exist" )
            continue
        fRead = f.readlines()
        fRead = ''.join( fRead )
        fRead = fRead + '\n'
        connection.send( fRead.encode() )
        connection.close()
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
        #TODO Support the download stream file for the dos format
        try:
            fileToOpen = dataRequest[1]
        except IndexError:
            connection.send( "you didn't specify a file to download\n".encode() )
            print( "[5] the peer didn't specify a file to download" )
            continue
        secondF = open( "../Downloads/" + dataRequest[ 1 ].decode(), "rb" )
        fDataRead = secondF.read().hex()
        f = open( "../Downloads/" + dataRequest[ 1 ].decode(), "rb" )
        fRead = f.readline()[0:2].decode()
        if fRead == 'MZ':
            connection.send( "the file exist, would you like to download the file?<yes/no>\n".encode() )
            downloadConfirmation = connection.recv( 1024 )
            if "yes" in downloadConfirmation.decode():
                #TODO fix the TypeError on the send(fDataRead)
                #print( "sending the file " + fDataRead )
                connection.send(fDataRead.encode())
                print( "uploading the dos file" )
            elif "no" in downloadConfirmation.decode():
                print( "the peer refused to download the dos file" )
            else:
                connection.send( "you didn't well specify the correct answer\n".encode() )
            connection.close()
        else:
            print( "the peer didn't request a DOS file\n" )
            connection.send( "you didn't specify a DOS file\n".encode() )
        
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
    elif item.decode() == None:
        connection.send( "you didn't specify a parameter try 0 <file>\n".encode() )
        print( "there is not parameter specified" )
        connection.close()
    else:
        connection.send( "the protocol is brokden, try 0 <file>\n".encode() )
        print( "wrong parameter has been specified" )
        connection.close()
s.close()

