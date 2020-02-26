#! /usr/bin/env python3
""" United States federal income tax calculations """
import datetime
import argparse
import sys
import t1040


def create_parse():
    """ create command line parser """
    parser = argparse.ArgumentParser(description="US individual tax calculator")
    parser.add_argument(
        "-v", "--verbose", help="increase verbosity", action="store_true"
    )
    return parser


def log(msg):
    """ output message to log """
    t = datetime.datetime()
    print(t.isoformat(), ": ", msg, file=sys.stderr)


def start():
    """ main event loop """
    parser = create_parse()
    args = parser.parse_args()
    if args.verbose:
        verbose = True
        log("Setting verbose mode.")
    else:
        verbose = False
    if verbose:
        log("Program started.")

    test = t1040.Return()
    test.taxpayer_name = "Joe Taxpayer"


if __name__ == "__main__":
    start()
