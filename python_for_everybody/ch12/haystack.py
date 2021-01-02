import re
file_name = "test_data.txt"
handle = open(file_name)
#Define lists for numbers in each line and all numbers in the file
numbers_in_line = None
all_numbers = []
for line in handle:
	numbers_in_line=re.findall('[0-9]+', line)
	if len(numbers_in_line) >0: 
		for number in numbers_in_line:
			all_numbers.append(int(number))
	#numbers= int(numbers)
	#sum(numbers)
print(all_numbers)

#Calculate total of all numbers
sum_of_numbers = sum(all_numbers)
print("total sum:")
print(sum_of_numbers)