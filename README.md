# python_click_comparison
Very simple code to look at path issues and click in Python.

I read a question that I understand as wanting to access a library without installing it. I think the proposed solution was to call into it as a command line command rather than importing and calling functions. To make that work, you need to pass in args and retrieve output from stdout. Click can do this when called with the subprocess library. CliRunner was suggested as a cleaner interface, but my understanding is that it would require importing.

I wrote some super simple code here to explore these issues for myself as well as possibly the discussion.
