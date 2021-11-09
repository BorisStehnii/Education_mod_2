def with_index(iter_, start=0):
    try:

        for el in iter_:
            res = (start, el)
            yield res
            start += 1
    except:
        res = (start, iter_)
        yield res


list_ = [1, 2, 4, 5]
print(list(with_index(3)))
print(list(with_index(list_)))
