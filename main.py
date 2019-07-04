import os
import glob
import time

from processes import BusyLogProcess, LazyLogProcess


def main():
    for logfile in glob.glob("test*.log"):
        print(f"Removing {logfile}")
        os.unlink(logfile)

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


if __name__ == "__main__":
    main()
