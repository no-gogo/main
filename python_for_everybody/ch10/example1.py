name = "mbox-short.txt"
handle = open(name)

# Make dictionary for histogram of people
#-----------------------------------------
people = dict()
person = None
# Get all emails from lines in the file
# that start with From, but not from
for line in handle:
    if "From" in line: 
        line = line.split()
        if ':' in line[0]:
            #do nothing
            shit=0
        else:
            # Assign current person name from line
            person = line[1]
          
            #Add person to dict if they are not already in it
            if person in people:
                people[person] = people[person] + 1
            else:
                people[person] = 1
                
                
# Find most frequent person

max_frequency = 0
most_frequent_person = None

for each_person in people:
    frequency = people[each_person]
    
    if frequency > max_frequency:
        most_frequent_person = each_person
        max_frequency=frequency
        
print(most_frequent_person, people[most_frequent_person])