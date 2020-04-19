#!/usr/bin/env python3
"""
Service launcher
"""

from subprocess import Popen
from subprocess import PIPE
from shlex import split
from typing import List


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


def kill_procs(procs: List[Popen]):
    for proc in procs:
        proc.kill()


def forever(num_procs: int = 2):
    procs = []

    for _ in range(num_procs):
        proc = run('python3 forever.py')
        procs.append(proc)

    indexes = list(range(num_procs))

    index_options = ','.join(indexes)

    while True:
        proc_index = input(f"Choose proc [{index_options}]: ")

        proc_index = int(proc_index)

        if proc_index == -1:
            break
        
        print(f"Chosen proc({proc_index})")
        proc = procs[proc_index]

        msg = input("Input for proc: ")

        output, errors = proc.communicate(msg)

        print(f"Output from proc({proc_index})")
        print(output)


def ask_forever():
    out = run('python3 forever.py')

    while out.poll() is None:
        msg = input("Need input: ")

        output, errors = out.communicate(msg)

        print((output,errors), end='')

    print(out.poll())


def run_no_in(command, log_file_name):
    cmd_seq = split(command)

    log_file = open(log_file_name, 'w+')

    proc = Popen(cmd_seq, stdout=log_file)

    return proc


def servers(num_procs: int = 2):
    procs = []

    for index in range(num_procs):
        port = 8000 + index
        logfile_name = f'server_{index}.log'
        proc = run_no_in(f'python3 server.py --port {port}', logfile_name)
        procs.append(proc)

    indexes = list(range(num_procs))

    index_options = ','.join(indexes)

    while True:
        proc_index = input(f"Choose proc [{index_options}]: ")

        proc_index = int(proc_index)

        if proc_index == -1:
            break
        
        print(f"Chosen proc({proc_index})")
        proc = procs[proc_index]

        msg = input("Command for proc: ")

        if msg == 'pid':
            pid = proc.pid
            print(f"PID: {pid}")

        elif msg == 'kill':
            print(f"Killing proc({proc_index})")
            proc.kill()

        elif msg == 'quit':
            print("Killing processes...")
            kill_procs(procs)

        else:
            print("Invalid command, skipping...")
            continue


def main(args):

    ask_forever()


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    args = parser.parse_args()
    main(args)
