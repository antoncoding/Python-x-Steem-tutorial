my_phone_book = {'myself':'0906882331', 'Alice':'876543219'}
print(my_phone_book['myself'])
print(my_phone_book['Alice'])
# print(my_phone_book['Bob'])

my_phone_book['Bob'] = '09080706053'
# or
my_phone_book.update({'Bob':'09080706023'})

my_phone_book.update({'Joey':'4738273643', 'Rachel':'8372381298', 'Monica':'8327192039'})

for key, value in my_phone_book.items():
    print('{} \t : {}'.format(key, value))

print(my_phone_book.keys())
