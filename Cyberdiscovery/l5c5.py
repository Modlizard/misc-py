#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#

import socket

# To make a connection to a TCP server:

# Create a socket. AF_INET means you're connecting to an IPv4 IP
#  Address.
# SOCK_STREAM means you are connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tell the socket what IP Address and Port number to connect to.
clientsocket.connect(('127.0.0.1', 8082))
# Send some data over the socket.
header = ( """
POST / HTTP/1.1
Host: 127.0.0.1
x-api-key: tweetbotkeyv1
""" )
data = "user=tweetbotuser&status-update=alientest"
contentLength = "Content-Length: " + str(len(data)) + "\r\n\r\n"
request = header+contentLength+data
clientsocket.send(request)
print(request)
# Receive some data back. The 1024 is the max number of bytes of data
# to accept.
data = clientsocket.recv(1024)
print(data)

#THIS BIT SHOULD SOLVE THE CHALLENGE ALONE
import urllib
import urllib2
data = {"user": "tweetbotuser", "status-update": "alientest"}
dataEncoded = urllib.urlencode(data)
request = urllib2.Request("http://127.0.0.1:8082",dataEncoded ,headers={"x-api-key" : "tweetbotkeyv1"})
contents = urllib2.urlopen(request).read()
print(contents)