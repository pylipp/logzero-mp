import multiprocessing
import time

from loguru import logger

# Uncomment to disable logging to stderr
# logger.remove(None)


LOGGER_CONFIG = dict(
    sink="test.log",
    rotation=120,  # to fit two log messages per file
    retention=5,
    enqueue=True,
)

logger.add(**LOGGER_CONFIG)

class BusyLogProcess(multiprocessing.Process):
    """A process that logs as fast as it can."""

    def run(self):
        while True:
            logger.info("a")


class LazyLogProcess(multiprocessing.Process):
    """A process that logs at a specific rate."""

    def run(self):
        for _ in range(1000):
            logger.warning("b")
            # Log at approx. 10 Hz
            time.sleep(0.1)
