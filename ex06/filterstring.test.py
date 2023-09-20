import unittest
import subprocess

class TestFilterString(unittest.TestCase):

    def run_script(self, args=None):
        command = ["python", "filterstring.py"]
        if args:
            command.extend(args)

        result = subprocess.run(command, text=True, capture_output=True, encoding="utf-8")
        return result.stdout

    def test_valid_input(self):
        test_args = ["Hello the World", "4"]
        expected_output = "['Hello', 'World']\n"
        output = self.run_script(args=test_args)
        self.assertEqual(output, expected_output)

    def test_empty_output(self):
        test_args = ["Hello the World", "99"]
        expected_output = "[]\n"
        output = self.run_script(args=test_args)
        self.assertEqual(output, expected_output)

    def test_incorrect_order(self):
        test_args = ["3", "Hello the World"]
        expected_output = "AssertionError: the arguments are bad\n"
        output = self.run_script(args=test_args)
        self.assertEqual(output, expected_output)

    def test_missing_arguments(self):
        expected_output = "AssertionError: the arguments are bad\n"
        output = self.run_script()
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
