


#Reads a file and shouts back each line in CAPS




import string

fhand = open('file.txt')

for line in fhand:
	line = string.upper(line)
	print(line)



