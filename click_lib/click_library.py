#!/usr/bin/env python3

import click
import sys

@click.command()
@click.option('--arg', default='default', help='enter some value')
def f(arg):
    print(f"hello from f() argument value is {arg}")
    print("no error", file=sys.stderr)
    return(0)

if __name__ == '__main__':
    retval = f()
    exit(retval)
