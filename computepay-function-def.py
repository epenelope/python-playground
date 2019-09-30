def computepay(h, r):
	if h <= 40:
		pay = h*r
		return pay
	elif h >= 40:
		pay = (h-40)*(r*1.5)+(40*r)
		return pay

rte = input("Enter hourly rate: ")
hrs = input("Enter week one hours: ")
h = float(hrs)
r = float(rte)

try:
	p1 = computepay(h, r)
	hrs = input("Enter week two hours: ")
	h = float(hrs)
	p2 = computepay(h, r)

except:
	print('Cannot compute non-numeric characters. Start over.')

print ("Gross pay for this pay period is $",p1+p2)









