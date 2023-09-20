import unittest
import subprocess
import ast

class TestHelloProcessing(unittest.TestCase):

    def run_hello_script(self):
        """Helper function to run the Hello.py script and capture its output."""
        result = subprocess.run(["python", "Hello.py"], capture_output=True, text=True)
        return result.stdout.strip().split('\n')

    def equivalent_outputs(self, output1, output2):
        """Check if two outputs are equivalent."""
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

    def test_case_1(self):
        captured_output = self.run_hello_script()

        expected_output = [
            "['Hello', 'World'] ",
            "('Hello', 'Germany')",
            "{'Heilbronn', 'Hello'}",
            "{'Hello': '42Heilbronn'}"
        ]

        if not self.equivalent_outputs(captured_output, expected_output):
            print("Captured Output:")
            for line in captured_output:
                print(line)
            print("\nExpected Output:")
            for line in expected_output:
                print(line)

        self.assertTrue(self.equivalent_outputs(captured_output, expected_output))


if __name__ == "__main__":
    unittest.main()
