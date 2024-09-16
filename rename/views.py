from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QThread
from collections import deque
from pathlib import Path

from .ui.window import Ui_Form
from .rename import Rename

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
    )
)

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self._files = deque()
        self._fileCount = len(self._files)
        self._setupUi()
        self._connectSignalsSlots()

    def _setupUi(self):
        self.setupUi(self)

    def _connectSignalsSlots(self):
        self.loadFilesButton.clicked.connect(self._loadFiles)
        self.renameFilesButton.clicked.connect(self.renameFiles)

    def _loadFiles(self):
        initDir = str(Path.home())
        self.dstFileList.clear()
        if self.dirEdit.text():
            initDir = self.dirEdit.text()
        files, filter = QFileDialog.getOpenFileNames(
            self, "Choose Files to Rename", initDir, filter=FILTERS
        )
        if len(files) > 0:
            fileExtension = filter[filter.index("*") : -1]
            self.extensionLabel.setText(fileExtension)
            srcDirName = str(Path(files[0]).parent)
            self.dirEdit.setText(srcDirName)
            for file in files:
                self._files.append(file)
                self.srcFileList.addItem(file)
            self._fileCount = len(self._files)

    def renameFiles(self):
        self._runRenameThread()

    def _runRenameThread(self):
        prefix = self.prefixEdit.text()
        self._thread = QThread()
        self._renamer = Rename(
            files=tuple(self._files),
            prefix=prefix
        )
        self._renamer.moveToThread(self._thread)
        # Rename the files
        self._thread.started.connect(self._renamer.run)
        # Update state
        self._renamer.signals.renamedFile.connect(self._updateStateWhenFileRenamed)
        # Clean up
        self._renamer.signals.finished.connect(self._thread.quit)
        self._renamer.signals.finished.connect(self._renamer.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        # Run the thread
        self._thread.start()

    def _updateStateWhenFileRenamed(self, newFile):
        self._files.popleft()
        self.srcFileList.takeItem(0)
        self.dstFileList.addItem(str(newFile))
