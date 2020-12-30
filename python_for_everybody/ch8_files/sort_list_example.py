# Care to debug?
debug=1
# Ask person for file
if not debug: fname = input("Enter file name: ")
if debug: fname = "romeo.txt"
# Read the file
fh = open(fname)
if debug: print("Opened file successfully.")
lst = list()
# Read each line in file
for (i,line) in enumerate(fh):
	for word in line.split(): lst.append(word.lower())
	if debug: print("Line ", i); print(line.rstrip()) 
if debug: print("Full list of words in file"); print(lst)
# Delete duplicate words.
lst = set(lst) 
if debug: print("No duplicates"); print(lst)
# Sort alphabetically
lst=sorted(lst, key=str.lower)
if debug: print("Sorted List:"); print(lst)