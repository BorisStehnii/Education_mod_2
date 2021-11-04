def with_index(iter_, start=0):
    for el in iter_:
        res = (start, el)
        yield res
        start += 1


list_ = [1, 2, 4, 5]
print(list(with_index(list_, 4)))
print(list(with_index(list_)))
