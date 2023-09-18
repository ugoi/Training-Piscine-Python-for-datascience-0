import sys
 
def whatis():
    # total arguments
    n = len(sys.argv)
    if (n == 1):
        sys.exit(0)
    elif (n != 2):
        print("AssertionError: more than one argument is provided")
        sys.exit(0)

    
    try:
        number: int = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)

    if (number % 2):
        print("I'm Odd.")
    else:
        print("I'm Even.")
    

 
if __name__ == "__main__":
    whatis()