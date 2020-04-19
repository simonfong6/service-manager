#!/usr/bin/env python3
"""
Service launcher
"""

from subprocess import Popen
from subprocess import PIPE
from shlex import split

def run(command):
    cmd_seq = split(command)

    proc = Popen(cmd_seq, stdout=PIPE, stdin=PIPE, universal_newlines=True)

    return proc

def ask():
    out = run('python3 ask.py')

    while out.poll() is None:
        msg = input("Need input: ")

        output, errors = out.communicate(msg)

        print(output, end='')

    print(out.poll())


def main(args):

    # procs = []

    # for _ in range(2):
    #     proc = Popen()

    # while True:
        
    pass

    # with open(output) as f:
    #     o = f.readlines()
    #     print(o)



if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    args = parser.parse_args()
    main(args)