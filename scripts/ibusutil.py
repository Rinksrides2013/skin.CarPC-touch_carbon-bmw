#! python
# Python IBUS/UDP Utilities for service.ibuspy

import xbmc
import socket

def sendRawHex(hex_data):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dest = ('127.0.0.1', 1805)
	if hex_data != "":
		xbmc.log("Sending datagram to IBUS bridge : " + hex_data, level=xbmc.LOGNOTICE)
		sock.sendto(hex_data.decode('hex'), dest)
	else:
		xbmc.log( "No data to send", level=xbmc.LOGNOTICE)     
