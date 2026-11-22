import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
)

from PySide6.QtGui import QPixmap, Qt

from styles.stylesheet import *

APP_VERSION = "0.1"

# TODO: Make PROD rdy
def main():

    app = QApplication(sys.argv)
    apply_global_stylesheet(app)

    window = Dashboard()

    window.show()
    sys.exit(app.exec())

class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segmentum Command - Total War")
        self.resize(1200, 750)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main horizontal layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(230)

        # Sidebar layout
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(15, 20, 15, 20)
        sidebar_layout.setSpacing(10)

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

        logo = QLabel("BATTLEFLEET")
        version = QLabel(f"FLEET SYSTEM v{APP_VERSION}")

        sidebar_layout.addWidget(self.logo)
        sidebar_layout.addWidget(logo)
        sidebar_layout.addWidget(version)
        sidebar_layout.addSpacing(30)


        # Right side content area
        self.content = QWidget()
        self.content.setObjectName("content")

        # Add widgets
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content, 1)

main()