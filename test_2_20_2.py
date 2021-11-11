import unittest

from exercise_2_20_1 import Open


class TestCaseEnter(unittest.TestCase):

    def setUp(self):
        self.file_name_true = "file_111.txt"
        self.file_name_new = "file.txt"
        self.file_name_not_type = "file"
        self.neg_file_name_new = "file_.txt"
        self.neg_file_name_not_type = "file_"
        self.command = "w"

    def test_file_true(self):
        with Open(self.file_name_true) as file:
            self.assertFalse(file.closed)
        self.assertTrue(file.closed)

    def test_file_new(self):
        with Open(self.file_name_new, command=self.command) as file:
            self.assertFalse(file.closed)
        self.assertTrue(file.closed)

    def test_file_not_type(self):
        with Open(self.file_name_not_type, command=self.command) as file:
            self.assertFalse(file.closed)
        self.assertTrue(file.closed)

    def test_neg_file_new(self):
        with self.assertRaises(FileNotFoundError):
            with Open(self.neg_file_name_new):
                pass

    def test_neg_file_false(self):
        with self.assertRaises(FileNotFoundError):
            with Open(self.neg_file_name_not_type):
                pass

