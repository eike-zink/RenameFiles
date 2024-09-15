from PySide6.QtWidgets import QWidget
from .ui.window import Ui_Form

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

