#!/usr/bin/env python3

# main.py in directory click2
# library.py is next-door in click, which is not installed or on the python path.


print("\n--- using subprocess  --")
import subprocess
proc = subprocess.Popen(['../click-lib/click-library.py', '--arg', 'some-arg-value'], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print(f"out: {out}")
print(f"err: {err}")
print(proc.returncode)


# The main objective: do this with Click, but without importing the library?


#              To Do




