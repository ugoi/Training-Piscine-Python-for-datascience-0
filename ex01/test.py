import sys
sys.path.append('../')  # Add the parent directory to the Python path
from stdout_tester import run_test
from unittest.mock import patch, Mock
from datetime import datetime

from format_ft_time import display_time  # Import the function

# Create a fixed "current" time
FIXED_NOW = datetime(2022, 1, 1, 12, 0, 0)  # e.g., Noon on January 1, 2022

class MockDateTime(datetime):
    @classmethod
    def now(cls, tz=None):
        return FIXED_NOW

def test_case_1():
    # Use patch to replace datetime.datetime in the format_ft_time module with our mock version
    with patch('format_ft_time.datetime', MockDateTime):
        display_time()

expected_output = '''Seconds since January 1, 1970: {0:,.4f} or {0:.2e} in scientific notation
Jan 01 2022
'''.format(FIXED_NOW.timestamp())

run_test(test_case_1, expected_output)
