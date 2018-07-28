def my_average(input_list):
    if len(input_list) < 2:
        print('We need a longer list!!!')
        return 0
    # 找出最大最小值
    max_num = input_list[0]
    min_num = input_list[0]
    for num in input_list:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    # 移除最大最小值
    input_list.remove(max_num)
    input_list.remove(min_num)
    # 再算一次平均
    all_sum = 0
    for num in input_list:
        all_sum = all_sum + num
    average = all_sum/len(input_list)
    return average

my_list = [1,8,3,6,2,345,-23,7]
answer = my_average(my_list)
print(answer)
