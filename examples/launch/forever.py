#!/usr/bin/env python3
"""
Asks the user for info.
"""


def say_hello_in_japanese(name):
    msg = f"Konnichiwa {name} san!"
    print(msg)


def main(args):

    while True:
        name = input("Please provide a name: ")

        if name == 'q':
            print("Stopping")
            break

        say_hello_in_japanese(name)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()


    args = parser.parse_args()
    main(args)