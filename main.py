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

# TODO: Make PROD rdy
def main():

    app = QApplication(sys.argv)
    with open("styles/main.qss", "r") as file:
        app.setStyleSheet(file.read())

    window = Dashboard()

    window.show()
    sys.exit(app.exec())

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Segmentum Command - Total War")



main()