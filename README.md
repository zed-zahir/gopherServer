# gopherServer script in python

how to use this script in debian based distro
```python
sudo ./main.py 127.0.0.1 70
```
or if you don't want to use the protocol in reserved tcp port, meaning without super user privileges
```python
./main.py 127.0.0.1 7000
```
in another terminal use
```bash
nc 127.0.0.1 70
```
then there would be a prompt use text file request, that's the only feature this script support for now
```bash
nc 127.0.0.1 70
=== Welcome to the Gopher server written in python by zahir meddour ===
0 sample.txt
The gopher server script is alive :D
0 hello.txt
can\'t open the file: hello.txt
2
the protocol is broken, try 0 <file>
```
Gopher RFC is: rfc1436

link: [rfc1436](https://www.ietf.org/rfc/rfc1436.txt)
