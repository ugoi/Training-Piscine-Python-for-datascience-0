import sys


def count_characters(sentence: str):
    """
    Count upper-case, lower-case, punctuation, digits, and spaces.
    """
    PUNCTUATION_CHARS = (
        r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"  # 'r' for raw string
    )

    counts = {
        "upper": sum(1 for c in sentence if c.isupper()),
        "lower": sum(1 for c in sentence if c.islower()),
        "punct": sum(1 for c in sentence if c in PUNCTUATION_CHARS),
        "space": sum(1 for c in sentence if c.isspace()),
        "digit": sum(1 for c in sentence if c.isdigit()),
        "total": len(sentence)
    }
    return counts


def get_sentence():
    """
    Prompt the user to provide a sentence.
    """
    sentence = ""
    while not sentence:
        try:
            sentence = input("What is the text to count?\n")
        except KeyboardInterrupt:
            sys.exit(0)
    return sentence


def main():
    """
    Main function to execute the program.
    """
    # total arguments
    n = len(sys.argv)
    if n == 1:
        sentence = get_sentence()
    elif n == 2:
        sentence = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return

    counts = count_characters(sentence)

    print(f'The text contains {counts["total"]} characters:')
    print(f'{counts["upper"]} upper letters')
    print(f'{counts["lower"]} lower letters')
    print(f'{counts["punct"]} punctuation marks')
    print(f'{counts["space"]} spaces')
    print(f'{counts["digit"]} digits')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
