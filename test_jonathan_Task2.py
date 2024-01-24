from unittest import TestCase
from JonathanTask2 import return_non_duplicate2


class Test(TestCase):
    def test_return_non_duplicate2(self):
        my_list = [4, 3, 2, 1, 1, 2, 2, 3]
        expected_result = 4
        result = return_non_duplicate2(my_list)
        self.assertEqual(result, expected_result)
