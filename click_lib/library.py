#!/usr/bin/env python3
import sys

def f(arg):
    print(f"hello from f() argument value is {arg}")

if __name__ == "__main__":
    if len(sys.argv) > 1 :
       f(sys.argv[1])
    exit(0)

