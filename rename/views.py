from PySide6.QtWidgets import QWidget, QFileDialog
from collections import deque
from pathlib import Path

from .ui.window import Ui_Form

FILTERS = ";;".join(
    (
        "PNG FIles (*.png)",
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

    def _loadFiles(self):
        self.dstFileList.clear()
        if self.dirEdit.text():
            intiDir = self.dirEdit.text()
        else:
            initDir = str(Path.home())
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

