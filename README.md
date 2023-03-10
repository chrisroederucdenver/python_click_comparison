# python_click_comparison
Very simple code to look at path issues and click in Python.

I read a question that I understand as wanting to access a library without installing it. I think the proposed solution was to call into it as a command line command rather than importing and calling functions. To make that work, you need to pass in args and retrieve output from stdout. Click can do this when called with the subprocess library. CliRunner was suggested as a cleaner interface, but my understanding is that it would require importing.

I wrote some super simple code here to explore these issues for myself as well as possibly the discussion.

## Description
There are two versions here. The first uses crude reference to argv to call library code as a second process rather than importing it. The second uses the click library and CliRunner. I think Nico's question invovles the difference between the click_main.py which is in a different directory and environment and calls the library in a different python process and different environment, and click_runner.py which uses the CliRunner, but has to be (I think) in the same directory.

- client
  - main.py
- lib
  -library.py

- click_client
  - click_main.py
- click_lib
  - click_library.py
  - click_runner.py

## To Run
I hard-coded some paths, so you have to cd down into the various directories.
- bash> cd client; ./main.py ; cd ..
- bash> cd click_client; ./click_main.py ; cd ..
- bash> cd click_lib; ./click_runner.py ; cd ..

