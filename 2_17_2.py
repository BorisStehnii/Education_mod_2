def custom_range(start, stop=0, step=1):
    if step > 0 and start > stop:
        start, stop = stop, start
    elif step < 0 and start > stop:
        while start > stop:
            yield start
            start += step
    while start < stop:
        yield start
        start += step


print(list(custom_range(13, 1, -2)))
print(list(custom_range(1, 10, 2)))
print(list(custom_range(3)))
print(list(custom_range(13, 10)))
