import unittest
import contextlib
from io import StringIO
from find_ft_type import all_thing_is_obj

class TestFindFtType(unittest.TestCase):

    def capture_all_thing_is_obj_output(self, obj):
        """Helper function to capture the output of all_thing_is_obj."""
        stdout_capture = StringIO()
        with contextlib.redirect_stdout(stdout_capture):
            all_thing_is_obj(obj)
        return stdout_capture.getvalue().strip()

    def test_case_1(self):
        ft_list = ["Hello", "tata!"]
        ft_tuple = ("Hello", "toto!")
        ft_set = {"Hello", "tutu!"}
        ft_dict = {"Hello" : "titi!"}

        captured_outputs = []
        captured_outputs.append(self.capture_all_thing_is_obj_output(ft_list))
        captured_outputs.append(self.capture_all_thing_is_obj_output(ft_tuple))
        captured_outputs.append(self.capture_all_thing_is_obj_output(ft_set))
        captured_outputs.append(self.capture_all_thing_is_obj_output(ft_dict))
        captured_outputs.append(self.capture_all_thing_is_obj_output("Brian"))
        # Specifically handle the integer case to capture the return value
        stdout_capture = StringIO()
        with contextlib.redirect_stdout(stdout_capture):
            result = all_thing_is_obj(10)
        captured_outputs.append(stdout_capture.getvalue().strip())
        if result is not None:
            captured_outputs.append(str(result))

        expected_output = [
            "List : <class 'list'>",
            "Tuple : <class 'tuple'>",
            "Set : <class 'set'>",
            "Dict : <class 'dict'>",
            "Brian is in the kitchen : <class 'str'>",
            'Type not found',
            '42'
        ]

        self.assertEqual(captured_outputs, expected_output)

if __name__ == "__main__":
    unittest.main()
