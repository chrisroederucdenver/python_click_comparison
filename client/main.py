#!/usr/bin/env python3



# Trying to run f from library without installing it here.
# Three efforts here are basically the same in that they run another Python process.

print("--- using os.system --")
import os
os.system( '../lib/library.py some-arg')


print("\n--- using os.popen --")
output = os.popen('../lib/library.py some-arg').read()
print(output)


print("\n--- using subprocess --")
import subprocess
proc = subprocess.Popen(['../lib/library.py', 'some-arg'], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print(f"out: {out}")
print(f"err: {err}")
print(proc.returncode)


