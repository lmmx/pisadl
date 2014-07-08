import os
for filename in os.listdir('.'):
	if len(filename.split('getxml'))>1:
		with open(filename,'w') as outputfile:
			spl = filename.split('-')
			sect = spl[0][-1:]
			subsect = spl[1].split('.')[0]
			interfacefile = 'interfaces'+sect+'-'+subsect+'.xml'
			scriptout = '#!/usr/bin/python\n\nimport urllib2\nimport re\nfrom datetime import datetime\nwith open("'+interfacefile+'","r+") as outputfile:\n\texecfile("download.py")\n'
			outputfile.write(scriptout)
