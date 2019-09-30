#CALCULATE GROSS PAY WITH OVERTIME:
hrs = input('How many hours did you work?')
rte = input('What is your hourly rate?')
try:
	hours = float(hrs)
	rate = float(rte)
	ot = (hours-40)*(rate*0.5)
	reg = hours*rate
	if hours <= 40:
		print(reg)
	else :
		print(ot+reg)
except:
	print('Cannot compute non-numeric characters. Starting over.')
	#okay, let's try that again!
	hrs = input('How many hours did you work?')
	rte = input('What is your hourly rate?')
	try:
		hours = float(hrs)
		rate = float(rte)
		ot = (hours-40)*(rate*0.5)
		reg = hours*rate
		if hours <= 40:
			print(reg)
		else :
			print(ot+reg)
	except:
		print('Error: Pay attention idiot. Integers only. One more try.')
		hrs = input('How many hours did you work?')
		rte = input('What is your hourly rate?')

		try:
			hours = float(hrs)
			rate = float(rte)
			ot = (hours-40)*(rate*0.5)
			reg = hours*rate
			if hours <= 40:
				print(reg)
			else :
				print(ot+reg)
		except:
			print('Error: Numeric input only. Too late dumbass, you had your chance! Goodbye.')



