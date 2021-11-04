class Filter:

    def __init__(self, func_, list_):
        self.func_ = func_
        self.list_ = list_
        self.ind_ = 0

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if isinstance(item, slice):
            self.start = item.start
            self.stop = item.stop
            if item.stop >= len(self.list_):
                self.stop = len(self.list_)
            res = []
            while self.start < self.stop:
                if self.func_(self.list_[self.start]):
                    res.append(self.list_[self.start])
                self.start += 1
            return res
        for _ in self.list_:
            if self.func_(self.list_[item]):
                return self.list_[item]
            else:
                item += 1
                continue

    def __next__(self):
        if self.ind_ < len(self.list_) and self.func_(self.list_[self.ind_]):
            res = self.list_[self.ind_]
            self.ind_ += 1
            return res
        elif self.ind_ < len(self.list_):
            self.ind_ += 1
        else:
            self.ind_ = 0
            raise StopIteration


li = [1, 2, 3, -4, -1, 5]
test_list = Filter(lambda x: x > 0, li)

for el in test_list:
    if el:
        print(el)

print(test_list[2:6])
