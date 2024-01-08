from collections import deque
import random
import string


def palindrom_check(arg):
    formatted_str = ''.join(char.lower()
                            for char in arg if char.isalnum())  # formats input str to make func insensible for upper case
    # and filteres out spases and special chars
    q = deque(formatted_str)  # adds input to the queue

    # checks if q is not empty, and then if chars [0] != [-1], it breakes loop, if whole str is a palondrom
    # it will run till the end, and func will return true
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


def main():
    input_str = "A man, a plan, a canal: Panama"
    print("Input String:", input_str)
    result = palindrom_check(input_str)
    print(f'Input string is a palindromic: {result}')


if __name__ == "__main__":
    main()
