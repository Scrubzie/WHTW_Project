import sys
from PySide6.QtWidgets import QApplication
from styles.stylesheet import *
from pages.dashboard import Dashboard

APP_VERSION = "0.1"

# TODO: Make PROD rdy
def main():

    app = QApplication(sys.argv)
    apply_global_stylesheet(app)

    window = Dashboard(app_version=APP_VERSION)

    window.show()
    sys.exit(app.exec())

main()