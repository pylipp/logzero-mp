## logzero and multiprocessing

This repo provides a Minimum Working Example to experiment with [`logzero`'s](https://github.com/metachris/logzero) capabilities in a multi-process context.

`logzero` claims to provide 'Robust and effective logging' featuring 'Multiple loggers can write to the same logfile (also across multiple Python files)'.

### Experiment

The main script sets up two processes. The first process logs at a very high rate, the second at a more moderate rate. Both processes log to the same file; and log-file rotation is set up using a very small maximum logfile size.

Since the first process logs very busily, it will rotate logs very often. Since the maximum logfile size is very small, rotation will also be triggered from the second process. However, a race condition in rotating the files might occur, and either process will complain about not being able to find a file it was about to move since it has just been moved by the other process.

### Dependencies

Tested using Python 3.6.5.

### Installation

Clone the repo and change into the new directory.

    python3.6 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

### Usage

    python main.py

### Outcome

Either of the involved processes will complain with

    --- Logging error ---
    Traceback (most recent call last):
      File "/usr/local/lib/python3.6/logging/handlers.py", line 72, in emit
        self.doRollover()
      File "/usr/local/lib/python3.6/logging/handlers.py", line 169, in doRollover
        os.rename(sfn, dfn)
    FileNotFoundError: [Errno 2] No such file or directory: '/home/pylipp/code/python/logzero-mp/test.log.2' -> '/home/pylipp/code/python/logzero-mp/test.log.3'

or

    --- Logging error ---
    Traceback (most recent call last):
      File "/usr/local/lib/python3.6/logging/handlers.py", line 72, in emit
        self.doRollover()
      File "/usr/local/lib/python3.6/logging/handlers.py", line 168, in doRollover
        os.remove(dfn)
    FileNotFoundError: [Errno 2] No such file or directory: '/home/pylipp/code/python/logzero-mp/test.log.5'

followed by

    Call stack:
      File "main.py", line 24, in <module>
        main()
      File "main.py", line 14, in main
        busy_log_process.start()
      File "/usr/local/lib/python3.6/multiprocessing/process.py", line 105, in start
        self._popen = self._Popen(self)
      File "/usr/local/lib/python3.6/multiprocessing/context.py", line 223, in _Popen
        return _default_context.get_context().Process._Popen(process_obj)
      File "/usr/local/lib/python3.6/multiprocessing/context.py", line 277, in _Popen
        return Popen(process_obj)
      File "/usr/local/lib/python3.6/multiprocessing/popen_fork.py", line 19, in __init__
        self._launch(process_obj)
      File "/usr/local/lib/python3.6/multiprocessing/popen_fork.py", line 73, in _launch
        code = process_obj._bootstrap()
      File "/usr/local/lib/python3.6/multiprocessing/process.py", line 258, in _bootstrap
        self.run()
      File "/home/pylipp/code/python/logzero-mp/processes.py", line 22, in run
        logger.info("a")
    Message: 'a'
    Arguments: ()
