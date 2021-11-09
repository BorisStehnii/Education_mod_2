import unittest
import json

from phonebook_2_18_2 import phonebook_2_18_2


class MyTestCaseAddNew(unittest.TestCase):

    def setUp(self):
        self.add_new = phonebook_2_18_2.add_new

    def test_str_add_new(self):
        self.assertEqual(self.add_new("1", "2", "3", "4"), {"1": {"first": "2", "last": "3", "full": "2 3", "city": "4"}})

    def test_int_add_new(self):
        with self.assertRaises(TypeError):
            self.add_new(1, 2, 3, 4)

    def test_bool_add_new(self):
        with self.assertRaises(TypeError):
            self.add_new(True, False, 3, 4)


class MyTestCaseAddToFile(unittest.TestCase):

    def setUp(self):
        self.add_to_file = phonebook_2_18_2.add_to_file
        self.entries_ = {"45": {"first": "35",
                                  "last": "2",
                                  "full": "35 2",
                                  "city": "sumy"}}

    def test_int_add_to_file(self):
        self.assertEqual(self.add_to_file(self.entries_, "tests_phonebook_2_18_2/Phonebook.json"), True)


class MyTestCaseSearch(unittest.TestCase):

    def setUp(self):
        self.search = phonebook_2_18_2.search
        self.entries_ = {"45": {"first": "35",
                                 "last": "2",
                                 "full": "35 2",
                                 "city": "sumy"}}
        with open("Phonebook.json", "w+") as phonebook:
            json.dump(self.entries_, phonebook, indent=4)

    def test_not_file_search(self):
        with self.assertRaises(FileNotFoundError):
            self.search("45", "Phone.json")

    def test_str_search(self):
        self.assertEqual(self.search("45", "tests_phonebook_2_18_2/Phonebook.json"), "45, {'first': '35', 'last': '2', 'full': '35 2', 'city': 'sumy'}")

    def test_not_str_search(self):
        self.assertEqual(self.search("5", "tests_phonebook_2_18_2/Phonebook.json"), False)


class MyTestCaseDelete(unittest.TestCase):

    def setUp(self):
        self.delete = phonebook_2_18_2.delete

    def test_int_delete(self):
        self.assertEqual(self.delete(345, "tests_phonebook_2_18_2/Phonebook.json"), False)

    def test_list_delete(self):
        self.assertEqual(self.delete("345", "tests_phonebook_2_18_2/Phonebook.json"), False)

    def test_dict_deleter(self):
        with self.assertRaises(TypeError):
            self.delete({4: 5}, "tests_phonebook_2_18_2/Phonebook.json")

    def test_not_file_deleter(self):
        with self.assertRaises(FileNotFoundError):
            self.delete(45, "Phone.json")


