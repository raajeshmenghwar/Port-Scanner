#!/bin/python3

import sys        # Library for reading command-line arguments
import socket     # Library for networking functionality
from datetime import datetime   # Library for working with dates and times

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translates hostname to ipv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    # If the user doesn't enter the correct command line arguments, the program will exit.

# Add a pretty banner
print("-"*50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
    for port in range(50,85):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set the socket timeout to 1 second
        socket.setdefaulttimeout(1)
        # Attempt to connect to the target on this port
        result = s.connect_ex((target,port))
        # Check if the connection was successful (port is open)
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
    # If the user interrupts the program, it will exit cleanly.

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
    # If the target hostname could not be resolved, the program will exit.

except socket.error:
    print("Could not connect to Server.")
    sys.exit()
    # If the program encounters a socket error, it will exit.

