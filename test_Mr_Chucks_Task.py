from unittest import TestCase
from mr_chucks_Task1 import return_duplicates


class Test(TestCase):
    def test_return_duplicate2(self):
        my_list = [2, 1, 1, 2, 2]
        expected_result = 2
        result = return_duplicates(my_list)
        self.assertEqual(result, expected_result)

    def test_return_duplicates(self):
        my_list = [3, 4, 5, 5]
        output = 5
        result = return_duplicates(my_list)
        self.assertEqual(result, output)
