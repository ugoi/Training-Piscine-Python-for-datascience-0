
import sys


def encode_to_morse(string: str) -> str:
    """Encode the given string to Morse code."""
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    if not all(x.isalnum() or x.isspace() for x in string):
        raise ValueError("Invalid arguments. String should contain only alphanumeric characters or spaces.")
    return " ".join(NESTED_MORSE[i.upper()] for i in string)
    

def main():
    """Main function to handle command-line arguments and print the Morse code representation."""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    input_string = sys.argv[1]

    try:
        print(encode_to_morse(input_string))
    except ValueError as e:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
