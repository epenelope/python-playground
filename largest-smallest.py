largest = None
smallest = None
while True:
	number = input('Enter a number: ')
	if number == 'done' : break
	try:
		num = float(number)
	except:
		print('Invalid input')
	if num >= largest:
		largest = num
	elif num <= smallest :
		smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)
