import shlex
import subprocess
import time

from watchdog import observers
from watchdog import events

class PipWatch(events.PatternMatchingEventHandler):
    def on_any_event(self, event):
        subprocess.check_call(shlex.split("pip install ."))

if __name__ == "__main__":

    event_handler = PipWatch("*.py")
    observer = observers.Observer()
    observer.schedule(event_handler, 'dstapi', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()