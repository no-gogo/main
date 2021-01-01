# Open the file, or just assume
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

# List of all emails
list=[]
shit =0
# Get all emails from lines in the file
# that start with From, but not from:
for line in fh:
    if "From" in line: 
        line = line.split()
        if ':' in line[0]:
            #do nothing
            shit=0
        else:
        	list.append(line[1])
        
#Remove duplicate names and count total
count =0
for email in list: 
    count +=1
    print(email)
print("There were", count, "lines in the file with From as the first word")