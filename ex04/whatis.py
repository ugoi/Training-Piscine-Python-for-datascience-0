import sys
 
def whatis():
    # total arguments
    n = len(sys.argv)
    if (n == 1):
        return
    elif (n != 2):
        print("AssertionError: more than one argument is provided")
        return

    
    try:
        number: int = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if (number % 2):
        print("I'm Odd.")
    else:
        print("I'm Even.")
    

 
if __name__ == "__main__":
    whatis()