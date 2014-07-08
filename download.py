#!/usr/bin/python

with open("interfaces.txt") as urllist:
	sect = int(outputfile.name.split('-')[0][-1:])
	subsect = int(outputfile.name.split('-')[1].split('.')[0])
	pdbcodes = re.findall('pdb_code>(.*)<', outputfile.read())
	num = len(pdbcodes)
	print str(num)+" interfaces have been written to file"
	startline = num/50 + (sect-1)*500  + (subsect-1)*50 + 1
	subsectendline = (sect-1)*500  + (subsect-1)*50 + 50
	now = datetime.now()
	if num/50 < 50:
		print str(now.hour)+":"+str(now.minute)+" - Starting at line "+str(startline)
		urltup = tuple(urllist)
		for line in urltup:
			if urltup.index(line)+1 >= startline and urltup.index(line)+1 <= subsectendline:
				url = line.rstrip()
				s = urllib2.urlopen(url)
				contents = s.read()
				outputfile.write(contents)
				now = datetime.now()
				print str(now.hour)+":"+str(now.minute)+" - "+str(urltup.index(line)+1)+" Downloaded "+url.split('?')[1]
	else:
		print "All interfaces downloaded."
