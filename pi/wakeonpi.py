#!/usr/bin/env python
# wakeonpi.py

import sys, getopt
import socket
import struct
import yaml
import re
import time
import tweepy

class MyStreamListener(tweepy.StreamListener):
	def on_direct_message(self, status):			
		m = re.match("^wol\s(.*)$", status.direct_message["text"], re.IGNORECASE)
		if m:
			wakeup(m.group(1))
		
	def on_error(self, status_code):
		if status_code == 420:
			time.sleep(300)
			#returning False in on_data disconnects the stream
			return False		

def wakeup(computer):
	computer = computer.upper().strip()
		
	if computer in computers:
		print "Waking computer", computer, "with MAC:", computers[computer]
		wake_on_lan(computers[computer])
	else:
		print "Unknown computer name", computer

def wake_on_lan(macaddress):
	""" Switches on remote computers using WOL. """

	# Check macaddress format and try to compensate.
	if len(macaddress) == 12:
		pass
	elif len(macaddress) == 12 + 5:
		sep = macaddress[2]
		macaddress = macaddress.replace(sep, '')
	else:
		raise ValueError('Incorrect MAC address format')
 
	# Pad the synchronization stream.
	data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
	send_data = '' 

	# Split up the hex values and pack.
	for i in range(0, len(data), 2):
		send_data = ''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])

	# Broadcast it to the LAN.
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.sendto(send_data, ('<broadcast>', 7))
    
def usage():
	print "wakeonpi.py -c <confFile>"
	sys.exit(2)
	
def main(argv):	
	confFile = ''
	confData = None
	
	# read command line arguments
	if len(argv) == 0: 
		usage()
		
	try:
		opts, args = getopt.getopt(argv, "c:", ["conf="])
	except getopt.GetoptError:
		usage()
		
	for opt, arg in opts:
		if opt in ("-c", "--conf"):
			confFile = arg
		
		
	# read and parse configuration file
	try:
		stream = open(confFile, "r")
		confData = yaml.load(stream)
		#stream.close()
	except IOError:
		print "Error reading configuration file."
		sys.exit(2)
	except:
		print "Error parsing YAML in configuration file."
		sys.exit(2)
			
	consumer_key = confData["twitter"]["consumer_key"]
	consumer_secret = confData["twitter"]["consumer_secret"]
	access_token = confData["twitter"]["access_token"]
	access_token_secret = confData["twitter"]["access_token_secret"]	
	
	global computers	
	computers = eval(repr(confData["computers"]).upper())
		
	# setup tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)
	
	while True:
				
		try:
			api = tweepy.API(auth)	
			print "Following twitter feed for: ", api.me().screen_name
			myStream = tweepy.Stream(auth, MyStreamListener())
			myStream.userstream(_with='user')
		
		except Exception, e:
			print "Error. Restarting Stream.... Error: "
			print e.__doc__
			print e.message
			time.sleep(15)

if __name__ == '__main__':	
	main(sys.argv[1:])