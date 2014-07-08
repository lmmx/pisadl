import os
for filename in os.listdir('.'):
	if len(filename.split('getxml'))>1:
		with open(filename,'w') as outputfile:
			spl = filename.split('-')
			sect = spl[0][-1:]
			subsect = spl[1].split('.')[0]
			interfacefile = 'interfaces'+sect+'-'+subsect+'.xml'
			scriptout = '#!/usr/bin/python\n\ntry:\n\timport urllib2\n\timport re\n\tfrom datetime import datetime\n\twith open("'+interfacefile+'","r+") as outputfile:\n\t\texecfile("download.py")\nexcept KeyboardInterrupt:\n\tpass\n'
			outputfile.write(scriptout)
