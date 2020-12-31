name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = {}
for line in handle:
    if "From" in line: 
        line = line.split()
        if ':' in line[0]:
            #do nothing
            shit=0
        else:
            
            # Get hr from time
            time = line[5]
            
            time = time.split(':')
            time = time[0]
            #print(time)
            # Tally the hour in count list
            if time in times:
                times[time] = times[time] + 1
            else:
                times[time] = 1
times = list(times.items())
times.sort()                
count = 0
for time in times: print(time[0], time[1])
#print(sorted(times))               
#print(sorted([(k,v) for (k,v) in times])