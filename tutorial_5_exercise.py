my_list = []
my_dictionary = {}
for n in range(1, 11):
    my_list.append(n*n*n)
    my_dictionary.update({n: n*n})

print(my_list)
print(my_dictionary)
