# This program reads a file line by line
# we calculate the average value for "X-DSPAM-Confidence"
# over all of the lines in the file.



import signal
import sys
import time
import threading


#Debug options. 1 = on, 0 = off
debug = 0


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main():

	# Ask what file we want to read and try to open it.
	while(1):
		try:	
			fname = raw_input("Enter file name: ")
			fh = open(fname)
			break

		except:
			print("Error reading that file!")
			print("Please try again.")

	# We are now goint to look for specific lines
	print("Searching for lines starting with: X-DSPAM-Confidence")
	
	# Count how many lines we find with the beginning we are looking to match
	count=0

	# Go through each line and look for match
	for line in fh:
	    if not line.startswith("X-DSPAM-Confidence:") : continue
	    if debug:
		    print(line) # print the line that was found
	    count=count+1 # if there is a match, add to count




# Explain program next steps
	print("Found "+ str(count) + " lines that started with X-DSPAM-Confidence")

	print("Calculating the average value of this line....")

if __name__ == "__main__":

# Setup to catch Ctrl-C
	signal.signal(signal.SIGINT, signal_handler)

# Do stuff
	main()

