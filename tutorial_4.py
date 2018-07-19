# While Loop with flag example
n = 1
m = 1312300
continue_to_loop = True
while continue_to_loop:
	n = n*2
	if n > m:
		print('Stop!')
		continue_to_loop = False

print(n)

# Easy Way
n =1
m = 1312300
while n < m:
	n = n*2

print(n)

# For loop
for i in range(15):
	print(i)

# For loop 2
shopping_list = ['apple', 'orange', 'lemon', 'Xiaomi 6 Plus', 'iPhoneX']
for item in shopping_list:
	print('{} is in your shopping list'.format(item))

