my_height = input('Please enter your height(M) : ')
my_weight = input('Please enter your weight(Kg): ')

my_height = float(my_height)
my_weight = float(my_weight)

BMI = my_weight/ (my_height*my_height)

if BMI > 24:
    print('You are overweight!')
elif BMI < 18:
    print('You are underweight!')
else:
    print('You are just fit!')



# if BMI > 24:
#     print('You are overweight!')
# else: # BMI < 24 的情況下
#     if BMI < 18:
#         print('You are underweight!')
#     else:
#         print('You are just fit!')

