#! /usr/bin/env python3
# pylint: disable=missing-module-docstring, missing-function-docstring
import datetime
import argparse
import sys
import t1040


def create_parse():
    parser = argparse.ArgumentParser(description="US individual tax calculator")
    parser.add_argument(
        "-v", "--verbose", help="increase verbosity", action="store_true"
    )
    return parser


def log(msg):
    t = datetime.datetime()
    print(t.isoformat(), ": ", msg, file=sys.stderr)


def start():
    parser = create_parse()
    args = parser.parse_args()
    if args.verbose:
        verbose = True
        log("Setting verbose mode.")
    else:
        verbose = False
    if verbose:
        log("Program started.")


if __name__ == "__main__":
    start()
