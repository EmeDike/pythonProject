from unittest import TestCase
from class_work import *;


class Test(TestCase):
    def test_rearrange_list(self):
        my_list = [42, 18, 41, 22, 12, 15]
        my_list2 =  [18, 42, 22, 41, 12, 15]
        result = rearrangeList(my_list)
        first_list_result, second_list_result = result
        self.assertEqual(my_list2,first_list_result)