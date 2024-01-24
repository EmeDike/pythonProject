from unittest import TestCase
from JonathanTask1 import return_non_duplicate

class Test(TestCase):
    def test_return_non_duplicate(self):
        my_list = [2, 2, 1, 3, 3]
        expected_result = 1
        result = return_non_duplicate(my_list)
        self.assertEqual(result, expected_result)
