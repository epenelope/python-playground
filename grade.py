score = input('Enter Score: ')
grade = float(score)
if grade>1:
	print('Invalid grade. Enter a number between 0 and 1')
elif grade>=0.9:
	print('A')
elif grade>=0.8:
	print('B')
elif grade>=0.7:
	print('C')
elif grade>=0.6:
	print('D')
else:
    print('F')
