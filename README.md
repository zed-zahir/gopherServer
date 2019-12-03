# gopherServer script in python

how to use this script in sudo based Unix like OS
```bash
$ cd server/
$ sudo ./server.py 127.0.0.1 70
```
or if you don't want to use the protocol in reserved tcp port, meaning without super user privileges
```bash
$ cd server/
$ ./server.py 127.0.0.1 7000
```
in another terminal use
```bash
$ ./client/client.py 127.0.0.1 70
```

if the file exist then it will print on the terminal

### or
```bash
$ ./client/client.py 127.0.0.1 70
```
if the file exist then there would be a prompt to accept or no

### or
```bash
$ ./client/client.py 127.0.0.1 70
```

Gopher RFC is: rfc1436

link: [rfc1436](https://www.ietf.org/rfc/rfc1436.txt)

here is the wikipedia article about the protocol

link [wikipedia Gopher protocol](https://en.wikipedia.org/wiki/Gopher_(protocol))
