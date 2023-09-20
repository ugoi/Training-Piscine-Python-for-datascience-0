import unittest
from unittest.mock import patch
from datetime import datetime
from io import StringIO
import contextlib

from format_ft_time import display_time  # Import the function directly

# Create a fixed "current" time
FIXED_NOW = datetime(2022, 1, 1, 12, 0, 0)  # e.g., Noon on January 1, 2022

class MockDateTime(datetime):
    @classmethod
    def now(cls, tz=None):
        return FIXED_NOW

class TestFormatFtTime(unittest.TestCase):

    def capture_display_time_output(self):
        """Helper function to capture the output of display_time."""
        stdout_capture = StringIO()
        with contextlib.redirect_stdout(stdout_capture):
            display_time()
        return stdout_capture.getvalue().strip()

    def test_case_1(self):
        # Use patch to replace datetime.datetime in the format_ft_time module with our mock version
        with patch('format_ft_time.datetime', MockDateTime):
            captured_output = self.capture_display_time_output()

        expected_output = '''Seconds since January 1, 1970: {0:,.4f} or {0:.2e} in scientific notation
Jan 01 2022
'''.format(FIXED_NOW.timestamp()).strip()

        self.assertEqual(captured_output, expected_output)

if __name__ == "__main__":
    unittest.main()
