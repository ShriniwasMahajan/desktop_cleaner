from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from event_handler import EventHandler

if __name__ == "__main__":
    watchPath = Path.home() / "OneDrive/Desktop"
    destinationRoot = Path.home() / "OneDrive/Desktop/Holder of Things"
    eventHandler = EventHandler(watchPath=watchPath, destinationRoot=destinationRoot)

    observer = Observer()
    observer.schedule(eventHandler, f"{watchPath}", recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
