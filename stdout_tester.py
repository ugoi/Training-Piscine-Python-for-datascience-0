import io
from contextlib import redirect_stdout

def run_test(test_func, expected_output):
    # Capture the outputs
    f = io.StringIO()
    with redirect_stdout(f):
        test_func()

    # Get the captured output
    out = f.getvalue()

    # Compare actual output against expected output
    if out == expected_output:
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected:")
        print(expected_output)
        print("Got:")
        print(out)