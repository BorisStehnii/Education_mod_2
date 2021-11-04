class TestIterable:

    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self.list_[item]


li_ = [1, 4, 5, 8]

test_li = TestIterable(li_)


print(test_li[2:5])

