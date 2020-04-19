#!/usr/bin/env python3
"""
Hello
"""


def say_hello(name):
    msg = f"Hello {name}!"
    print(msg)


def main(args):
    say_hello(args.name)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument(
        '--name',
        type=str,
        required=True)

    args = parser.parse_args()
    main(args)