# You aren't limited to using raw sockets to make network connections.
# Python can make HTTP requests quite easily.

# First you'll need to import the urllib2 module.
import urllib2

# Then you need to open the URL:
response = urllib2.urlopen("http://127.0.0.1:8080")

# Now you just need to read the contents of the response:
html = response.read()
print(html)

# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
# the response.

response2 = urllib2.urlopen("http://127.0.0.1:8080/winning")
html2 = response2.read()
print(html2)

from time import sleep

# Sockets are a way of sending data over a network.
# There are two main types of sockets, TCP and UDP.
# Which to use depends on the application you are communicating with.

# You will need to import the socket library first.
import socket

# To make a connection to a TCP server:

# Create a socket. AF_INET means you're connecting to an IPv4 IP
#  Address.
# SOCK_STREAM means you are connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tell the socket what IP Address and Port number to connect to.
clientsocket.connect(('127.0.0.1', 9987))
# Send some data over the socket.
clientsocket.send('hello')
# Receive some data back. The 1024 is the max number of bytes of data
# to accept.
data = clientsocket.recv(1024)
print(data)

# You should see "You said: hello" printed out. That's because our
# server is setup to respond to whatever you send it by adding
# You said: to the front of it and sending it back.

# To make a TCP Server:

# Create a socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to listen to a port.
serversocket.bind(("127.0.0.1", 9985))
# Tell the socket to start listening.
# The 10 is the maximum number of connections.
serversocket.listen(10)

# Setup an infinite loop so the socket will keep listening for
# incoming connections.
while True:
    # If it gets a new connection, accept it and save the connection
    # and address.
    connection, address = serversocket.accept()
    # Read 1024 bytes of data from the connection.
    data = connection.recv(1024)
    # Check the length of data. If the length is more than 0 then
    # that means something was sent, so print it out.
    if len(data) > 0:
        print("Received: " + data)

    # Close the connection.
    connection.close()
    # We don't need to keep listening any more so break out of the
    # infinite loop
    break

# Close the socket.
serversocket.close()

sleep(0.05)

# CHALLENGE 1: Write a TCP Client that will connect to 127.0.0.1 on
#              port 9990.
#              Your client must send "Knock, knock" to the server.
#              Then get the response, and print it out.
clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket2.connect(('127.0.0.1', 9990))
clientsocket2.send("Knock, knock")
data = clientsocket2.recv(1024)
print(data)

# Working with files is a common task for a programming language
# Python makes it easy. Let's look at an example:

myfile = open("/tmp/newfile.txt", "w")

# Open a file called newfile.txt in /tmp. If no file exists it will be
# created.
# The "w" is the mode, in this case "w" is for write. You could use "r"
# for read.
# There are various other modes we will cover them briefly later.

myfile.write("Here is my message.\n")
myfile.write("Here is my second message.")

# Write "Here is my message\n" to the file you opened. \n is a
# newline character.
# You need to add a \n every time you want to add a new line,
# otherwise everything will be on one line.

myfile.close()

# Since we opened the file, we need to close it when we're done with it.

# There are many different modes for opening a file in Python.
# Here are just a few useful ones:
# w - Allows you to write to a file only. If the file exists, it will
# be overwritten.
# r - Allows you to read the file only.
# r+ - Allows you to read and write to the file.
# w+ - Allows you to read and write to the file, but if the file
# already exists it will overwrite it.
# a - Allows you to append to the file
# (write to the end of an existing file)
# a+ - Allows you to append to the file, and read from the file.

myfile = open("/tmp/newfile.txt", "r")
filecontents = myfile.read()
print(filecontents)
myfile.close()

# Here we are reading the file we created previously.

# You can also use the 'with' syntax. It's better.
# Here is an example of reading a file line by line instead of all
# at once.

with open("/tmp/newfile.txt", "r") as myfile:
    for line in myfile:
        print(line)

# The major benefit of using 'with' is that it handles closing the
# file for you.
# We used a for loop to read the file line by line.

# CHALLENGE 1: Write a for loop that will create a file called
#              /tmp/cars.txt. There should be 50 lines of text in the
#              file. The first line should be "There are 0 cars"
#              and 1 car should be added every line. Until
#              the last line which should read "There are 49 cars"
with open("/tmp/newfile2.txt", "w") as myfile2:
  for x in range(0,50):
    print("There are " + str(x) + " cars")
# CHALLENGE 2: Open the file at /tmp/cars.txt and read the contents.
#              Print the contents to the screen.

import urllib2
for x in range(5499,5601):
	request = urllib2.Request("http://127.0.0.1:8082", headers={"x-api-key" : x})
	contents = urllib2.urlopen(request).read()
	print(contents)