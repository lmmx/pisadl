#!/usr/bin/python

try:
	import urllib2
	import re
	from datetime import datetime
	with open("interfaces4-8.xml","r+") as outputfile:
		execfile("download.py")
except KeyboardInterrupt:
	pass
