# Python Port Scanner
This is a simple port scanner written in Python that takes an IP address as a command-line argument and scans for open ports between 50 and 85. It prints out the results and handles errors such as invalid arguments and connection failures

## Usage
To use the scanner, run the following command:


## Copy code
python3 scanner.py <ip_address>
Replace <ip_address> with the IP address of the target machine you want to scan.

## Requirements
This program was built using Python 3 and tested on Kali Linux. It should work on other Unix-based operating systems as well. If you want to use this on Windows, you may need to install a Unix-like environment such as Cygwin or WSL.

## How to Use on Windows
To use this program on Windows, you can follow these steps:

- Install Python 3 on your machine by downloading it from the official website: https://www.python.org/downloads/
- Open a command prompt by pressing Win + R, typing cmd, and hitting Enter.
- Navigate to the directory where you have saved scanner.py.
- Run the scanner using the command python scanner.py <ip_address>.
- Replace <ip_address> with the IP address of the target machine you want to scan.
