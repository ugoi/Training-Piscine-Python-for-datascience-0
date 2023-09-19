import sys
sys.path.append('../')  # Add the parent directory to the Python path
from building import count_characters, main
from stdout_tester import run_test

# ... [the initial imports and function definitions remain unchanged]

def test_count_characters():
    print("Running test_count_characters...")
    test_input = (
        "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. "
        "Python 2 was discontinued with version 2.7.18 in 2020."
    )
    expected_output = {
        "upper": 2,
        "lower": 121,
        "punct": 8,
        "space": 25,
        "digit": 15,
        "total": 171
    }
    actual_output = count_characters(test_input)
    if actual_output == expected_output:
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected:", expected_output)
        print("Got:", actual_output)

def test_main_with_arg():
    print("Running test_main_with_arg...")
    sys.argv = ["building.py", "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."]
    expected_output = (
        "The text contains 171 characters:\n"
        "2 upper letters\n"
        "121 lower letters\n"
        "8 punctuation marks\n"
        "25 spaces\n"
        "15 digits\n"
    )
    run_test(main, expected_output)  # Assuming `run_test` function handles the print for success or failure.

def test_main_with_prompt():
    print("Running test_main_with_prompt...")
    # Use io.StringIO() to emulate input() function
    import io
    input_value = 'Hello World! '
    sys.stdin = io.StringIO(input_value)
    sys.argv = ["building.py"]
    expected_output = (
        "What is the text to count?\n"
        "The text contains 13 characters:\n"
        "2 upper letters\n"
        "8 lower letters\n"
        "1 punctuation marks\n"
        "2 spaces\n"
        "0 digits\n"
    )
    run_test(main, expected_output)  # Assuming `run_test` function handles the print for success or failure.

if __name__ == "__main__":
    test_count_characters()
    test_main_with_arg()
    test_main_with_prompt()
