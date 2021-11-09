class MFilter():

    def remove_positives(self, list_):
        new_list = [x for x in list_ if x < 0]
        return new_list


class MMath():

    def square_nums(self, list_):
        new_list = [x**2 for x in list_]
        return new_list

    def filter_leaps(self, list_):
        new_list = [year for year in list_ if not year % 4 and year % 100 or not year % 400]
        return new_list


class Mathematician(MFilter, MMath):
    pass

if __name__ == '__main__':
    m = Mathematician()
    print(m.square_nums([7, 6, -5]))
    print(m.remove_positives([2, 5, -7, -8]))
    print(m.filter_leaps([2000, 2001, 1884, 1995, 2003, 2020, 1100, 2100]))
