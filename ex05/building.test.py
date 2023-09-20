import unittest
import subprocess

class TestBuilding(unittest.TestCase):

    def run_script(self, input_data=None, args=None):
        command = ["python", "building.py"]
        if args:
            command.extend(args)

        result = subprocess.run(command, input=input_data, text=True, capture_output=True, encoding="utf-8")
        return result.stdout

    def test_count_characters(self):
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
        from building import count_characters
        actual_output = count_characters(test_input)
        self.assertEqual(actual_output, expected_output)

    def test_main_with_arg(self):
        test_arg = ["Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."]
        expected_output = (
            "The text contains 171 characters:\n"
            "2 upper letters\n"
            "121 lower letters\n"
            "8 punctuation marks\n"
            "25 spaces\n"
            "15 digits\n"
        )
        output = self.run_script(args=test_arg)
        self.assertEqual(output, expected_output)

    def test_main_with_prompt(self):
        input_data = 'Hello World! '
        expected_output = (
            "What is the text to count?\n"
            "The text contains 13 characters:\n"
            "2 upper letters\n"
            "8 lower letters\n"
            "1 punctuation marks\n"
            "2 spaces\n"
            "0 digits\n"
        )
        output = self.run_script(input_data=input_data)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
