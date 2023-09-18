import sys
sys.path.append('../')  # Add the parent directory to the Python path
from Hello import process_data  # Import the function
from io import StringIO
import contextlib
import ast

# Capture the output from the function and return it
def capture_output(func):
    stdout_capture = StringIO()
    with contextlib.redirect_stdout(stdout_capture):
        func()
    return stdout_capture.getvalue().strip().split('\n')

# Check if two outputs are equivalent
def equivalent_outputs(output1, output2):
    for line1, line2 in zip(output1, output2):
        if line1.startswith("{") and line1.endswith("}") and line2.startswith("{") and line2.endswith("}"):
            # Treat as sets
            set1 = ast.literal_eval(line1)
            set2 = ast.literal_eval(line2)
            if set1 != set2:
                return False
        else:
            if line1.strip() != line2.strip():
                return False
    return True

def test_case_1():
    captured_output = capture_output(process_data)

    expected_output = [
        "['Hello', 'World'] ",
        "('Hello', 'Germany')",
        "{'Heilbronn', 'Hello'}",
        "{'Hello': '42Heilbronn'}"
    ]

    if equivalent_outputs(captured_output, expected_output):
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected:")
        for line in expected_output:
            print(line)
        print("\nGot:")
        for line in captured_output:
            print(line)

if __name__ == "__main__":
    test_case_1()
