import sys
sys.path.append('../')  # Add the parent directory to the Python path
from stdout_tester import run_test
import whatis

def simulate_argv(args):
    """
    Simulate command line arguments by modifying sys.argv
    """
    sys.argv = ['whatis.py'] + args

def test_no_args():
    """
    Test the scenario when no arguments are provided
    """
    simulate_argv([])
    whatis.whatis()

def test_even_number():
    """
    Test with an even number argument
    """
    simulate_argv(['14'])
    whatis.whatis()

def test_odd_number():
    """
    Test with an odd number argument
    """
    simulate_argv(['-5'])
    whatis.whatis()

def test_zero():
    """
    Test with zero as the argument
    """
    simulate_argv(['0'])
    whatis.whatis()

def test_non_integer():
    """
    Test with a non-integer argument
    """
    simulate_argv(['Hi!'])
    whatis.whatis()

def test_multiple_args():
    """
    Test with multiple arguments
    """
    simulate_argv(['13', '5'])
    whatis.whatis()

if __name__ == "__main__":
    run_test(test_no_args, "")
    run_test(test_even_number, "I'm Even.\n")
    run_test(test_odd_number, "I'm Odd.\n")
    run_test(test_zero, "I'm Even.\n")
    run_test(test_non_integer, "AssertionError: argument is not an integer\n")
    run_test(test_multiple_args, "AssertionError: more than one argument is provided\n")
