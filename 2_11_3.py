def func_1(nums):
    return [num**2 for num in nums]


def func_2(nums):
    return [num for num in nums if num > 0]


def func(list_, f_1, f_2):
    negative_list = [x for x in list_ if x < 0]
    if len(negative_list) > 0:
        func_res = f_2
    else:
        func_res = f_1
    return func_res(list_)


list_exam_1 = [1, 2, 3, -4]
list_exam_2 = [1, 2, 3, 4]
print(list_exam_1)
print(func(list_exam_1, func_1, func_2))
print(15*"_")
print(list_exam_2)
print(func(list_exam_2, func_1, func_2))
