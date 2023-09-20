import unittest
import subprocess

class TestSosApplication(unittest.TestCase):

    def run_sos_app(self, input_str):
        """Helper function to run the sos.py script and capture its output."""
        result = subprocess.run(["python", "sos.py", input_str], capture_output=True, text=True)
        return result.stdout.strip()

    def test_valid_string(self):
        self.assertEqual(self.run_sos_app("sos"), "... --- ...")

    def test_string_with_numbers(self):
        self.assertEqual(self.run_sos_app("sos1"), "... --- ... .----")

    def test_string_with_spaces(self):
        self.assertEqual(self.run_sos_app("so s"), "... --- / ...")

    def test_string_with_invalid_characters(self):
        output = self.run_sos_app("so$s")
        self.assertEqual(output, "AssertionError: the arguments are bad")


    def test_uppercase_string(self):
        self.assertEqual(self.run_sos_app("SOS"), "... --- ...")

    def test_mixed_case_string(self):
        self.assertEqual(self.run_sos_app("SoS"), "... --- ...")

if __name__ == "__main__":
    unittest.main()
