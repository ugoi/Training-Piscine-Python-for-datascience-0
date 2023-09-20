import unittest
from ft_filter import ft_filter

class TestFtFilter(unittest.TestCase):

    def test_filter_odd_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = [2, 4]
        result = list(ft_filter(lambda x: x % 2 == 0, numbers))
        self.assertEqual(result, expected_result)

    def test_filter_empty_strings(self):
        strings = ["apple", "", "banana", "", "cherry"]
        expected_result = ["apple", "banana", "cherry"]
        result = list(ft_filter(lambda x: x != "", strings))
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
