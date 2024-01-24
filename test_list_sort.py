from unittest import TestCase
from list_sort import list_sort

class test(TestCase):
    def test_return_non_duplicate2(self):
        my_list = [4, 3, 2, 1, 1, 2, 2, 3]
        expected_result = 4
        result = list_sort(my_list)
        self.assertEqual(result, expected_result)

    def test_unpack_list(self):
        my_list = [1]
        expected_result = 1
        result = list_sort(my_list)
        self.assertEqual(result, expected_result)

    def test_return_non_duplicate(self):
        my_list = [2, 2, 1, 3, 3]
        expected_result = 1
        result = list_sort(my_list)
        self.assertEqual(result, expected_result)
