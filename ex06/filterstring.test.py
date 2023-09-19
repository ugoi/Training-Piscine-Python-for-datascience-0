import sys
sys.path.append('../')  # Add the parent directory to the Python path
from stdout_tester import run_test
from filterstring import main

# Modify the sys.argv to simulate command line arguments
def test_valid_input():
    sys.argv = ["filterstring.py", "Hello the World", "4"]
    main()

def test_empty_output():
    sys.argv = ["filterstring.py", "Hello the World", "99"]
    main()

def test_incorrect_order():
    sys.argv = ["filterstring.py", "3", "Hello the World"]
    main()

def test_missing_arguments():
    sys.argv = ["filterstring.py"]
    main()

if __name__ == "__main__":
    print("Running test_valid_input...")
    run_test(test_valid_input, "['Hello', 'World']\n")

    print("\nRunning test_empty_output...")
    run_test(test_empty_output, "[]\n")

    print("\nRunning test_incorrect_order...")
    run_test(test_incorrect_order, "AssertionError: the arguments are bad\n")

    print("\nRunning test_missing_arguments...")
    run_test(test_missing_arguments, "AssertionError: the arguments are bad\n")
