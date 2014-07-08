import urllib2
import re
from datetime import datetime #this allows you to drop the leading `datetime.` and makes slightly more concise cf. just import datetime
with open("interfaces1-3.xml","r+") as outputfile:
	execfile('download.py')
