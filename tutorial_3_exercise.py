a = input('Please enter the first number: ')
b = input('Please enter the second number: ')
c = input('Please enter the last number: ')

a = float(a)
b = float(b)
c = float(c)

if a > b:
	if a >c :
		print(a)
	else: 
		print(c)
else: 
	if b > c:
		print(b)
	else:
		print(c)
