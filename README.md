## xprocess-test

Testing pytest-xprocess running a TCP server in Docker.

## Instructions to reproduce

1. `$ docker build -t xprocess-test .`
2. `$ docker run -it --rm --entrypoint "/bin/bash" -v "$PWD:/opt" xprocess-test`
3. (in container) `# pipenv shell`
4. (in container) `# pytest tests/`

## Observed Behavior

 - When running `# pytest tests/`, pytest hangs.

I just noticed here, that when pressing `ctrl-c` and running `# pytest tests/` again, it does seem to complete successfully in Docker, but this seems to be because the server is still running in the background, as observed in the following logs

```bash
$ docker run -it --rm --entrypoint "/bin/bash" -v "$PWD:/opt" xprocess-test
root@c8b75f9a4ffb:/opt# pipenv shell
Launching subshell in virtual environment…
root@c8b75f9a4ffb:/opt#  . /root/.local/share/virtualenvs/opt-zvmYt2-H/bin/activate
(opt) root@c8b75f9a4ffb:/opt# pytest tests/
====================================================================== test session starts =======================================================================
platform linux -- Python 3.8.6, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /opt
plugins: cov-2.10.1, xprocess-0.15.0
collected 1 item

tests/server_test.py ^C

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! KeyboardInterrupt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
/root/.local/share/virtualenvs/opt-zvmYt2-H/lib/python3.8/site-packages/xprocess.py:215: KeyboardInterrupt
(to show a full traceback on KeyboardInterrupt use --full-trace)
===================================================================== no tests ran in 37.67s =====================================================================
(opt) root@c8b75f9a4ffb:/opt# ps aux | grep host_sim
root          13  0.0  0.4  12208  9280 pts/1    S    17:07   0:00 /root/.local/share/virtualenvs/opt-zvmYt2-H/bin/python -m xprocess_test.host_sim
(opt) root@c8b75f9a4ffb:/opt# pytest tests/
====================================================================== test session starts =======================================================================
platform linux -- Python 3.8.6, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /opt
plugins: cov-2.10.1, xprocess-0.15.0
collected 1 item

tests/server_test.py .                                                                                                                                     [100%]

======================================================================= 1 passed in 0.02s ========================================================================
```
