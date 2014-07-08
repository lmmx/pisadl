#!/usr/bin/python

import urllib2
import re
from datetime import datetime
with open("interfaces1-1.xml","r+") as outputfile:
	execfile("download.py")
