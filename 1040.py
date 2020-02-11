#! /usr/bin/env python3
#pylint: disable=missing-module-docstring, missing-function-docstring
import datetime
import argparse
import sys

def create_parse():
    parser = argparse.ArgumentParser(
        description='US individual tax calculator')
    parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true")
    return parser

def log(msg):
    t = datetime.datetime()
    print(t.isoformat(), ": ", msg, file=sys.stderr)

#brackets = min, max, base, rate

#2019
#MFS, SS
#0, 19400, 0,.10
#19400,78950, 1940,.12
#78950,168400,9086,.22
#168400,321450,28765,.24
#321450,408200,65497,.32
#408200,612350,93257,.35
#612350,,165709.50,.37

#HH
#0,13850,0,.10
#13850,52850,1385,.12
#52850,84200,6065,.22
#84200,160700,12962,.24
#160700,204100,31322,.32
#204100,510300,45210,.35
#510300,,152380,.37

#S
#0,9700,0,.10
#9700,39475,970,.12
#39475,84200,4543,.22
#84200,160725,14382.5,.24
#160725,204100,32748.5,.32
#204100,510300,46628.5,.35
#510300,,153798.5,.37

#MFS
#0,9700,0,.10
#9700,39475,970,.12
#39475,84200,4543,.22
#84200,160725,14382.5,.24
#160725,204100,32748.5,.32
#204100,306175,46628.5,.35
#306175,,82354.75,.37

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

if __name__ == '__main__':
    start()
