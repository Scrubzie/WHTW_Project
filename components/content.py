from PySide6.QtWidgets import QStackedWidget

class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("content")