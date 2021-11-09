import unittest

from exercise_2_18_1.ex_2_18_1 import MMath


class TestCaseSquareNums(unittest.TestCase):

    def setUp(self):
        self.square_nums = MMath().square_nums

    def test_list_square_nums(self):
        self.assertEqual(self.square_nums([7, 6, 5]), [49, 36, 25])

    def test_list_neg_square_nums(self):
        self.assertEqual(self.square_nums([-7, 6, -5]), [49, 36, 25])

    def test_dict_square_nums(self):
        self.assertEqual(self.square_nums({6: "3", 5: 5, -4: 2}), [36, 25, 16])

    def test_list_str_square_nums(self):
        with self.assertRaises(TypeError):
            self.square_nums([5, 6, "4"])

    def test_int_square_nums(self):
        with self.assertRaises(TypeError):
            self.square_nums(5)

    def test_str_square_nums(self):
        with self.assertRaises(TypeError):
            self.square_nums("4, 3, 2")


class TestCaseFilterLeaps(unittest.TestCase):

    def setUp(self):
        self.filter_leaps = MMath().filter_leaps

    def test_list_filter_leaps(self):
        self.assertEqual(self.filter_leaps([2000, 1884, 2003, 2020, 2100]), [2000, 1884, 2020])

    def test_list_neg_filter_leaps(self):
        self.assertEqual(self.filter_leaps([-2000, 1884, 2003, 2020, 2100]), [1884, 2020])

    def test_list_str_filter_leaps(self):
        with self.assertRaises(TypeError):
            self.filter_leaps([2000, 1884, 2003, 2020, "2100"])

    def test_dict_filter_leaps(self):
        with self.assertRaises(TypeError):
            self.filter_leaps({2000: "d", 1884: "c"})

    def test_int_filter_leaps(self):
        with self.assertRaises(TypeError):
            self.filter_leaps(2000)

    def test_str_filter_leaps(self):
        with self.assertRaises(TypeError):
            self.filter_leaps("2000")


# if __name__ == '__main__':
#     unittest.main()
