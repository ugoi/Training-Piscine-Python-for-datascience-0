import sys
sys.path.append('../')  # Add the parent directory to the Python path

from NULL_not_found import NULL_not_found
from stdout_tester import run_test

def test_case_1():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))

expected_output_1 = '''Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
'''

run_test(test_case_1, expected_output_1)

# from NULL_not_found import NULL_not_found
# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))