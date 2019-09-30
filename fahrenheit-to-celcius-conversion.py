try:
	fahrenheit_temp = input('Enter Fahrenheit Temperature: ')
	f = float(fahrenheit_temp)
	c = (f - 32.0) * 5.0 / 9.0	
	print('Celsius = ', c)
except:
	print ('Please enter an integer')
try:
	fahrenheit_temp = input('Enter Fahrenheit Temperature: ')
	f = float(fahrenheit_temp)
	c = (f - 32.0) * 5.0 / 9.0	
	print('Celsius = ', c)
except:
	print ('That was not an integer. Start over.')

