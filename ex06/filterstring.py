import sys
from ft_filter import ft_filter


def main():
    """
    Main function to execute the program.
    """
    # total arguments
    n = len(sys.argv)
    if n != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        s = str(sys.argv[1])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    split = s.split()

    filt = list(ft_filter(lambda s: len(s) > n, split))

    print(filt)


if __name__ == "__main__":
    main()
