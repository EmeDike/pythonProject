from unittest import TestCase
from Jonathan_Taskday2 import list_with_additional_number


class Test(TestCase):
    def test_add_a_number_to_the_array1(self):
        my_list = [1, 2, 3]
        expected_result = [1, 2, 4]
        result = list_with_additional_number(my_list)
        self.assertEqual(result, expected_result)

    def test_add_a_number_to_the_array2(self):
        my_list = [4, 3, 2, 1]
        expected_result = [4, 3, 2, 2]
        result = list_with_additional_number(my_list)
        self.assertEqual(result, expected_result)

    def test_add_a_number_to_the_array3(self):
        my_list = [9]
        expected_result = [1, 0]
        result = list_with_additional_number(my_list)
        self.assertEqual(result, expected_result)