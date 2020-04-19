#!/usr/bin/env python3
"""
Service launcher
"""

import subprocess




def main(args):
    out = subprocess.run(["python3", "hello.py", "--name", "Jenn"], capture_output=True)
    print(out)

    with open('bruh.txt' , 'w') as f:
        out = subprocess.run(["python3", "hello.py", "--name", "Jenn"], stdout=f)
        print(out)

    out = subprocess.run(["python3", "ask.py"], input="Simon", text=True)
    print(out)
    print("Hello World")


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    args = parser.parse_args()
    main(args)