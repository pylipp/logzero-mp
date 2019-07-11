import os
import glob
import time

from loguru import logger

from processes import BusyLogProcess, LazyLogProcess


LOGGER_CONFIG = dict(
    sink="test.log",
    rotation=120,  # to fit two log messages per file
    retention=5,
    enqueue=True,
)

def main():
    for logfile in glob.glob("test*.log"):
        print(f"Removing {logfile}")
        os.unlink(logfile)

    # Set up logger
    print(logger._handlers)
    # Uncomment to disable logging to stderr
    logger.remove(None)

    logger.add(**LOGGER_CONFIG)

    # Alternatively, configure logger. This removes existing handlers
    # logger.configure(handlers=[LOGGER_CONFIG])

    busy_log_process = BusyLogProcess()
    busy_log_process.start()

    # Let BusyLogProcess create some logfiles
    time.sleep(0.1)

    lazy_log_process = LazyLogProcess()
    lazy_log_process.start()

    # Let program work for a bit, then shut down
    time.sleep(1)
    lazy_log_process.terminate()
    busy_log_process.terminate()

    print(logger._handlers)


if __name__ == "__main__":
    main()
