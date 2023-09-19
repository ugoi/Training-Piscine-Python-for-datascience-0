from ft_filter import ft_filter

# Tests for ft_filter (adjusted for iterator behavior)
def test_ft_filter():
    # Test 1: Filtering out odd numbers
    numbers = [1, 2, 3, 4, 5]
    expected_result_1 = [2, 4]
    assert list(ft_filter(lambda x: x % 2 == 0, numbers)) == expected_result_1

    # Test 2: Filtering out empty strings
    strings = ["apple", "", "banana", "", "cherry"]
    expected_result_2 = ["apple", "banana", "cherry"]
    assert list(ft_filter(lambda x: x != "", strings)) == expected_result_2

    return "All tests passed!"

def main():
    test_ft_filter()

if __name__ == "__main__":
    main()