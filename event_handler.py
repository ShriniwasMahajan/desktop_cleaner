import shutil
import os
import datetime
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from extensions import extensionPaths
from typing import Union


def addDateToPath(path: Path, fileStat: Union[os.stat_result, None]):
    if not fileStat:
        creationTime = datetime.today()
    else:
        creationTime = datetime.datetime.fromtimestamp(fileStat.st_ctime)

    datedPath = path / f"{creationTime.year}" / f"{creationTime.month:02d}"
    datedPath.mkdir(parents=True, exist_ok=True)
    return datedPath


def renameFile(source: Path, destinationPath: Path):
    if Path(destinationPath / source.name).exists():
        increment = 1

        while True:
            increment += 1
            newName = destinationPath / f"{source.stem}_{increment}{source.suffix}"

            if not newName.exists():
                return newName
    else:
        return destinationPath / source.name


class EventHandler(FileSystemEventHandler):
    def __init__(self, watchPath: Path, destinationRoot: Path):
        self.watchPath = watchPath.resolve()
        self.destinationRoot = destinationRoot.resolve()

    def on_modified(self, event):
        for child in self.watchPath.iterdir():
            if child.is_file and child.suffix.lower() in extensionPaths:
                fileStat = os.stat(child)
                destinationPath = (
                    self.destinationRoot / extensionPaths[child.suffix.lower()]
                )
                destinationPath = addDateToPath(path=destinationPath, fileStat=fileStat)
                destinationPath = renameFile(
                    source=child, destinationPath=destinationPath
                )
                shutil.move(src=child, dst=destinationPath)
