from unittest import TestCase
from JonathanTask2 import return_non_duplicate2
from JonathanTask3 import unpack_list


class Test(TestCase):
    def test_unpack_list(self):
        my_list = [1]
        expected_result = 1
        result = unpack_list(my_list)
        self.assertEqual(result, expected_result)
