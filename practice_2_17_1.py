def custom_filter(func, list_):
    for li_ in list_:
        if func(li_):
            yield li_


li = [1, 2, 3, -4, -1, 5]
print(list(custom_filter((lambda x: x > 0), li)))


custom_filter_2 = (li_ for li_ in li if li_ > 0)
result = []
for el in custom_filter_2:
    result.append(el)
print(result)
