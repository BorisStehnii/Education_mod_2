import unittest


from exercise_2_18_1.ex_2_18_1 import MFilter


class TestCaseRemovePositives(unittest.TestCase):

    def setUp(self):
        self.remove_positives = MFilter().remove_positives

    def test_list_remove_positives(self):
        self.assertEqual(self.remove_positives([5, 6, 7, 8]), [])

    def test_list_neg_remove_positive(self):
        self.assertEqual(self.remove_positives([5, -6, 7]), [-6])

    def test_dict_remove_positive(self):
        self.assertEqual(self.remove_positives({6: "3", 5: 5, -4: 2}), [-4])

    def test_list_str_remove_positive(self):
        with self.assertRaises(TypeError):
            self.remove_positives([5, 6, "4"])

    def test_int_remove_positive(self):
        with self.assertRaises(TypeError):
            self.remove_positives(5)

    def test_str_remove_positive(self):
        with self.assertRaises(TypeError):
            self.remove_positives("4, 3, 2")






# if __name__ == '__main__':
#     unittest.main()
