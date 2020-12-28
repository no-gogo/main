



# Use the file name mbox-short.txt as the file name

while(1):
	try:
		fname = raw_input("Enter file name: ")
		fh = open(fname)
		break
	except:
		print("Error reading that file!")
		print("Please try again.")
	except KeyBoardInterrupt:
		print("Interrupted!")


print("Searching for lines starting with: X-DSPAM-Confidence")

count=0


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    count=count+1
print("Found "+ count + " lines that started with X-DSPAM-Confidence")
print()
print("Calculating the average value of this line....")







