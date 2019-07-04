## loguru and multiprocessing

This repo provides a Minimum Working Example to experiment with [`loguru`'s](https://github.com/Delgan/loguru) capabilities in a multi-process context.

`loguru` claims to provide 'enjoyable logging' featuring 'Easier file logging with rotation / retention' and 'Multiprocess-safe'.

### Experiment

The main script sets up two processes. The first process logs at a very high rate, the second at a more moderate rate. Both processes log to the same file; and log-file rotation is set up using a very small maximum logfile size.

loguru internally enqueues messages coming from the different processes, logs them, and rotates the log file accordingly.

### Dependencies

Tested using Python 3.6.5 on Ubuntu 16.04.

### Installation

Clone the repo and change into the new directory.

    python3.6 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

### Usage

    python main.py

### Outcome

Messages are logged to file and console (stderr).
