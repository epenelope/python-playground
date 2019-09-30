#assigns user input, which answers the prompt "Enter Fahrenheit Temperature:"), with the variable 'inp'
inp = input('Enter Fahrenheit Temperature: ')
try:
	#this next line converts the string (which is how the user input 	is interpreted by python) to a floating point integer.
	fahr = float(inp)
	#now, the conversion math...
	cel = (fahr - 32.0) * 5.0 / 9.0
	#user sees:
	print(cel)
#but what happens if the user enters something that isn't a number?
except:
	print ('Please enter an number')
	inp = input('Enter Fahrenheit Temperature:')
	fahr = float(inp)
	#now, the conversion math...
	cel = (fahr - 32.0) * 5.0 / 9.0
	#user sees:
	print(cel)
