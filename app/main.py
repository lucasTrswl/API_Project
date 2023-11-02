import sys
import bdd_constants
import psycopg2
import models
import psycopg2.extras


def print_hi(name):
    """

    :type name: object
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def main():
    print("main function call")
    print("main function end")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi(sys.path)
    main()
