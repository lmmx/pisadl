#!/usr/bin/python

import urllib2
import re
from datetime import datetime
with open("interfaces1-5.xml","r+") as outputfile:
	execfile("download.py")
