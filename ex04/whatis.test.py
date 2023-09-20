import unittest
import sys
import io
import whatis

def simulate_argv(args):
    """
    Simulate command line arguments by modifying sys.argv
    """
    sys.argv = ['whatis.py'] + args

class TestWhatis(unittest.TestCase):

    def setUp(self):
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_no_args(self):
        simulate_argv([])
        whatis.whatis()
        self.assertEqual(self.held_output.getvalue(), "")

    def test_even_number(self):
        simulate_argv(['14'])
        whatis.whatis()
        self.assertEqual(self.held_output.getvalue(), "I'm Even.\n")

    def test_odd_number(self):
        simulate_argv(['-5'])
        whatis.whatis()
        self.assertEqual(self.held_output.getvalue(), "I'm Odd.\n")

    def test_zero(self):
        simulate_argv(['0'])
        whatis.whatis()
        self.assertEqual(self.held_output.getvalue(), "I'm Even.\n")

    def test_non_integer(self):
        simulate_argv(['Hi!'])
        whatis.whatis()
        self.assertEqual(self.held_output.getvalue(), "AssertionError: argument is not an integer\n")

    def test_multiple_args(self):
        simulate_argv(['13', '5'])
        whatis.whatis()
        self.assertEqual(self.held_output.getvalue(), "AssertionError: more than one argument is provided\n")

if __name__ == "__main__":
    unittest.main()
