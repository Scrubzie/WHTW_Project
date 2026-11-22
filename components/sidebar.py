from datetime import datetime
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, Qt

class Sidebar(QWidget):

    def __init__(self, app_version):
        super().__init__()
        self.setObjectName("sidebar")
        self.sidebar_layout = QVBoxLayout(self)

        self.app_version = app_version
        self.init_ui()

    def init_ui(self):
        # Sidebar
        self.setObjectName("sidebar")
        self.setFixedWidth(230)

        # Sidebar layout
        self.sidebar_layout.setContentsMargins(15, 20, 15, 20)
        self.sidebar_layout.setSpacing(10)

        self.init_header()
        self.sidebar_layout.addSpacing(30)
        self.init_navigation()
        self.sidebar_layout.addStretch()
        self.init_footer()

    def init_header(self):
        topbar = QHBoxLayout()

        self.logo = QLabel()
        pixmap = QPixmap("assets\\images\\icon.png")

        self.logo.setPixmap(
            pixmap.scaled(
                75,
                75,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        self.logo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        logo = QLabel("SEGMENTUM\nCOMMAND")
        version = QLabel(f"Total War v{self.app_version}")
        topbar.addWidget(self.logo)
        topbar.addWidget(logo)

        self.sidebar_layout.addLayout(topbar)
        self.sidebar_layout.addWidget(version)

    def init_navigation(self):
        button1 = QPushButton("Thing1")
        self.sidebar_layout.addWidget(button1)
        button2 = QPushButton("Thing2")
        self.sidebar_layout.addWidget(button2)
        button3 = QPushButton("Thing3")
        self.sidebar_layout.addWidget(button3)
        button4 = QPushButton("Thing4")
        self.sidebar_layout.addWidget(button4)
        button5 = QPushButton("Thing5")
        self.sidebar_layout.addWidget(button5)

    def init_footer(self):
        footer = QLabel(
            f"© {datetime.now().year} A. Mann. All rights reserved."
        )

        self.sidebar_layout.addWidget(footer)