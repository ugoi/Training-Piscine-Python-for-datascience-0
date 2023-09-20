import unittest
import contextlib
from io import StringIO
from NULL_not_found import NULL_not_found

class TestNULLNotFound(unittest.TestCase):

    def capture_output(self, obj):
        """Helper function to capture the output of NULL_not_found."""
        stdout_capture = StringIO()
        with contextlib.redirect_stdout(stdout_capture):
            result = NULL_not_found(obj)
        # Combine captured output and the return value (if any)
        captured = [stdout_capture.getvalue().strip()]
        if result is not None:
            captured.append(str(result))
        return captured

    def test_case_1(self):
        # Variables for testing
        Nothing = None
        Garlic = float("NaN")
        Zero = 0
        Empty = ''
        Fake = False
        
        # List of variables to test
        test_objects = [Nothing, Garlic, Zero, Empty, Fake, "Brian"]

        # Expected outputs
        expected_output = [
            "Nothing: None <class 'NoneType'>", '0',
            "Cheese: nan <class 'float'>", '0',
            "Zero: 0 <class 'int'>", '0',
            "Empty: <class 'str'>", '0',
            "Fake: False <class 'bool'>", '0',
            "Type not Found", "1"
        ]

        # Collect all the outputs
        captured_outputs = [out for obj in test_objects for out in self.capture_output(obj)]
        
        self.assertEqual(captured_outputs, expected_output)

if __name__ == "__main__":
    unittest.main()
