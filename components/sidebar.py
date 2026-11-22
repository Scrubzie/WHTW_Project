from datetime import datetime
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, Qt

class Sidebar(QWidget):

    def __init__(self, app_version, content_widget):
        super().__init__()
        self.setObjectName("sidebar")
        self.sidebar_layout = QVBoxLayout(self)

        self.app_version = app_version
        self.content_widget = content_widget
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
        logo.setObjectName("logo")
        version = QLabel(f"Total War v{self.app_version}")
        version.setObjectName("version")
        topbar.addWidget(self.logo)
        topbar.addWidget(logo)

        self.sidebar_layout.addLayout(topbar)
        self.sidebar_layout.addWidget(version)

    def init_navigation(self):

        navigation = [
                    ("Dashboard", 0),
                    ("Ship Constructor", 1),
                    ("Ship Database", 2),
                    ("Factions", 3),
                    ("Fleet Builder", 4),
                    ("Lua Exporter", 5),
                ]
        
        self.nav_buttons = {}

        for name, index in navigation:

            button = QPushButton(name)
            button.setObjectName("navButton")

            button.clicked.connect(
                lambda checked=False, i=index:
                self.change_page(i)
            )

            self.sidebar_layout.addWidget(button)
            self.nav_buttons[index] = button

    def init_footer(self):
        footer = QLabel(
            f"© {datetime.now().year} A. Mann. All rights reserved."
        )
        footer.setObjectName("footer")

        self.sidebar_layout.addWidget(footer)

    def change_page(self, index):
        self.content_widget.setCurrentIndex(index)

        for button_index, button in self.nav_buttons.items():
            is_active = button_index == index

            button.setProperty("active", "true" if is_active else "false")

            # Refresh stylesheet
            button.style().unpolish(button)
            button.style().polish(button)
            button.update()