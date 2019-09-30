largest = None
smallest = None
#here comes a loop
while True:
	number = input('Enter a number: ')
	if number == 'done' : break #the loop ends when the user enters 'done'
	try: #if the user enters something other than 'done' the program tries to convert the input to a float integer 
		num = float(number) 
	except: #if the input is other than an integer
		print('Invalid input')
	#now we compare each integer that goes through the loop to the previous one, determining the largest and smallest
	if num >= largest:	
		largest = num
	elif num <= smallest :
		smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)
