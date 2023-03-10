#!/usr/bin/env python3

# click_library.py and click_runner.py in same directory, same python path
# The goal of this project is to figure out how to use the library without installing
# it in the same place as the runner client. This has not achieved that, but shows
# CliRunner in this context.

print("\n--- using click test  --")
from click.testing import CliRunner
from click_library import f  # requires click-library.py to be on the Python path!

def test_click_lib():
    runner = CliRunner()
    result = runner.invoke(f, ['--arg', 'click-arg-value-example'])
    print(f"exit code is {result.exit_code}")
    print(f"output is \"{result.output}\"")
    assert result.exit_code == 0
    #assert result.stdout == 'hello from f() argument value is click-arg-value-example\n'
    #assert result.stderr == 'no error\n'
    assert result.output == 'hello from f() argument value is click-arg-value-example\nno error\n'

test_click_lib()


