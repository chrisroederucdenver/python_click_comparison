#!/usr/bin/env python

# main.py in directory click2
# library.py is next-door in click, which is not installed or on the python path.

# requires installation in the local env
##from library import f
##f(6)


# trying to run f from library without installing it here.
# One way is  os.system, though it gets odd and criticize when you get into retrieving the output
print("--- using os.system --")
import os
os.system( '../click/library.py some-arg')


print("\n--- using os.popen --")
output = os.popen('../click/library.py some-arg').read()
print(output)


print("\n--- using subprocess --")
import subprocess
#proc = subprocess.Popen(['../click/library.py', 'some-arg'], stdout=subprocess.PIPE, shell=TRUE)
proc = subprocess.Popen(['../click/library.py', 'some-arg'], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print(f"out: {out}")
print(f"err: {err}")
print(proc.returncode)


