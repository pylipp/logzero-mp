import multiprocessing
import time

from loguru import logger


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
