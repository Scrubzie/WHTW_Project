from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QFrame

class ShipListPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("ship_list_panel")

        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.panel = QFrame()
        self.panel.setObjectName("ship_list_panel_background")

        self.panel_layout = QVBoxLayout(self.panel)
        self.panel_layout.addWidget(QLabel("Ship List Panel"))

        self.main_layout.addWidget(self.panel)