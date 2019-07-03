import multiprocessing
import time

import logzero


LOGGER_CONFIG = dict(
    logfile="test.log",
    maxBytes=72,  # to fit two log messages per file
    backupCount=5,
)


class BusyLogProcess(multiprocessing.Process):
    """A process that logs as fast as it can."""

    def run(self):
        logger = logzero.setup_logger("busy", disableStderrLogger=True,
                                      **LOGGER_CONFIG)

        while True:
            logger.info("a")


class LazyLogProcess(multiprocessing.Process):
    """A process that logs at a specific rate."""

    def run(self):
        logger = logzero.setup_logger("lazy", **LOGGER_CONFIG)

        for _ in range(1000):
            logger.warn("b")
            # Log at approx. 10 Hz
            time.sleep(0.1)
