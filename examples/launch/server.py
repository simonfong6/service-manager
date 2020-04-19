#!/usr/bin/env python3
"""
Backend server.
"""
import logging

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


def main(args):

    logging.basicConfig(filename=args.log_file)

    app.run(
        host='0.0.0.0',
        debug=args.debug,
        port=args.port
    )


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-p', '--port',
                        help="Port that the server will run on.",
                        type=int,
                        default=8000)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False,
                        action='store_true')

    parser.add_argument('--log_file',
                        help="Log File")

    args = parser.parse_args()
    main(args)
