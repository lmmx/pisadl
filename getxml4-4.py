#!/usr/bin/python

import urllib2
import re
from datetime import datetime
with open("interfaces4-4.xml","r+") as outputfile:
	execfile("download.py")