# Print Basic Info
def print_basic_info(name, age, country):
    print('My name is {}'.format(name))
    print('I\'m {} years old.'.format(age))
    print('I\'m from {}'.format(country))

print_basic_info('Anton', 22, 'no where')
print_basic_info('Sanchez', 28, 'Spain')
print_basic_info('Lilian', 18, 'United State')


# BMI
def calculate_BMI(height, weight):
    bmi = weight/(height*height)
    return bmi

def print_warnings(bmi):
    print('Your BMI is {}'.format(bmi))
    message = 'You are just fit!'
    if bmi < 17:
        message = 'You are underweight!'
    elif bmi > 23:
        message = 'You are overweight!'
    print(message)

user_height = float(input('Please enter your height: '))
user_weight = float(input('Please enter your weight: '))
bmi = calculate_BMI(user_height, user_weight)
print_warnings(bmi)
