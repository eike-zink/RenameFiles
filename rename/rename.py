"""This module provides the Rename class to rename multiple files"""

import time

from pathlib import Path
from PySide6.QtCore import QObject, Signal

class RenameSignals(QObject):
    progressed = Signal(int)
    renamedFile = Signal(Path)
    finished = Signal()

class Rename(QObject):
    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix
        self.signals = RenameSignals()

    def run(self):
        for fileNumber, file in enumerate(self._files, 1):
            newFile = file.parent.joinpath(
                f'{self._prefix}{str(fileNumber)}{file.prefix}'
            )
            file.rename(newFile)
            time.sleep(0.1)  # TODO überprüfen, warum diese Funktion benötigt wird
            self.signals.progressed.emit(fileNumber)
            self.signals.renamedFile.emit(newFile)
        self.signals.progressed.emit(0)
        self.signals.finished.emit()