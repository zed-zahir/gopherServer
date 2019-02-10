#!/usr/bin/python3

import socket
import os
import sys
import time

# Global Variables
PATH = "../Download/"

# check the parameters

if len( sys.argv ) < 3:
    print( "script as sgopher server\nusage: ./script.py <ip address> <tcp port>")
    #exit if the parameters are not adapted
    sys.exit()

# create the socket, listen and bind

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( ( sys.argv[ 1 ], int( sys.argv[ 2 ] ) ) )
s.listen( 1 )

# create the loop to make the script as a daemon

while 1:

    # retrive the connection and the client informations from the accept() function

    connection, client = s.accept()

    # welcome message

    connection.send( "=== Welcome to the Gopher server written in python by zahir meddour ===\n".encode())
    
    # grab the connection informations and log with print() function

    request = connection.recv( 1024 )
    dataRequest = request.split()
    print( client, dataRequest )
    
    # try to catch the out of boundary error
    
    try:
        item = dataRequest[ 0 ]
    except IndexError:
        connection.send( "internal error\n".encode() )
        print( "internal error" )
        break

    # check the first byte of the client request

    if item.decode() == "0":

        # try to catch the out of boundary error

        try:
            fileToOpen = dataRequest[1]
        except IndexError:
            connection.send( "you didn't specify a file to open\n".encode() )
            print( "[0] the peer didn't specify a file to open" )
            continue

        # grabe the file to open from the client request 

        fileToOpen = dataRequest[ 1 ]

        # catch the open file if broken

        try:
            f = open( PATH + fileToOpen.decode() )
        except:
            fileNotFound = "file: \"" + fileToOpen.decode() + "\" not found\n"
            connection.send( fileNotFound.encode() )
            print( "file the peer try access \"" + fileToOpen.decode() +"\" doesn't exist" )
            continue

        # read the file from the disk, make it as a string format

        fRead = f.read()
        fRead = ''.join( fRead )
        fRead = fRead + '\n'

        # send the data back to the client

        connection.send( fRead.encode() )
        connection.close()

    # support the Gopher SubMenu with the parameter '1'

    elif item.decode() == "1":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    
    # support the CCSO Nameserver feature
    
    elif item.decode() == "2":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
   
    # support the feature "Error code returned by a Gopher server to indicate failure" 

    elif item.decode() == "3":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )

    # support the feature "BinHex-encoded file (primarily for Macintosh computers)" 

    elif item.decode() == "4":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )

    # support DOS file feature 

    elif item.decode() == "5":
        #TODO Support the download stream file for the dos format
        
        # catch the out of boundary index
        
        try:
            fileToOpen = dataRequest[1]
        except IndexError:
            connection.send( "you didn't specify a file to download\n".encode() )
            print( "[5] the peer didn't specify a file to download" )
            continue

        # open the file for the data to send

        secondF = open( PATH + dataRequest[ 1 ].decode(), "rb" )
        fDataRead = secondF.read().hex()

        # open the file to check the authencity of the dos format

        f = open( PATH + dataRequest[ 1 ].decode(), "rb" )
        fRead = f.read()[0:2].decode()
        if fRead == 'MZ':

            # confirm the file exist and send the hint message
            
            connection.send( "the file exist, would you like to download the file?<yes/no>\n".encode() )
            downloadConfirmation = connection.recv( 1024 )
            if "yes" in downloadConfirmation.decode():
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
        
    # support the feature "uuencoded file" 

    elif item.decode() == "6":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    
    # support the feature "Gopher full-text search"
    
    elif item.decode() == "7":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    
    # support the tenet feature 
    
    elif item.decode() == "8":
        #TODO Support this feature
        connection.send( "this feature is not supported yet\n".encode() )
    
    # support the "Binary file" feature
    
    elif item.decode() == "9":
        #TODO Support the download stream file for the dos format
        
        # catch the out of boundary index
        
        try:
            fileToOpen = dataRequest[1]
        except IndexError:
            connection.send( "you didn't specify a file to download\n".encode() )
            print( "[9] the peer didn't specify a file to download" )
            continue

        # open the file in read and binary mode

        f = open( PATH + dataRequest[ 1 ].decode(), "rb" )
        connection.send( "the file exist\n".encode() )
        
        # hexify and send the data
        
        fDataRead = f.read().hex()
        connection.send(fDataRead.encode())
        connection.close()

    # other conditions if the magic byte is not the correct one

    else:
        connection.send( "the protocol is brokden, try 0 <file>\n".encode() )
        print( "wrong parameter has been specified" )
        connection.close()
s.close()

