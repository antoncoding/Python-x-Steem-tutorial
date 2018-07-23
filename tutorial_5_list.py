my_todo_list = ['Homework', 'Write on Steem', 'Get a haircut']
count_todo = len(my_todo_list)
print('I have {} tasks on my todo list today! They are:'.format(count_todo))
for todo in my_todo_list:
    print(todo)

print(my_todo_list)
my_todo_list.append('Watch a movie')
my_todo_list.append('Sleep')
count_todo = len(my_todo_list)
print('I have {} tasks on my todo list now!'.format(count_todo))

print(my_todo_list)
my_todo_list.remove('Write on Steem')
my_todo_list.remove('Homework')
print(my_todo_list)

print(my_todo_list[1])
