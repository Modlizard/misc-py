from zipfile import ZipFile
for x in range (0, 10):
	for y in range (0, 10):
		for z in range (0, 10):
			with ZipFile('alien-zip-2092.zip') as zf:
				password = (str(x)+str(y)+str(z))
				print(password)
				try:
					zip_file.extractall(pwd=password)
					password = 'Password found: %s' % password
				except:
					pass