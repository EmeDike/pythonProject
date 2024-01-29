from unittest import TestCase
from list_weekend_practice import calculate_products


class Test(TestCase):
    def test_manipulate_list(self):
        input_list = [1, 2, 3, 4]
        expected_result = [24, 12, 8, 6]
        result = calculate_products(input_list)
        self.assertEqual(result, expected_result)
