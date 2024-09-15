"""This module provides functionality for renaming files."""

import sys

from PySide6.QtWidgets import QApplication

from .views import Window

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
