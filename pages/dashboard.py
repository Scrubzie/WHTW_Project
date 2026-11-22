from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from components import Content, Sidebar

class Dashboard(QMainWindow):

    def __init__(self, app_version):
        super().__init__()

        self.app_version = app_version
        self.setObjectName("dashboard")
        self.content = Content()
        self.sidebar = Sidebar(self.app_version, self.content)

        self.init_window()
        self.init_ui()
        #self.init_connections()
        

    def init_window(self):
        self.setWindowTitle("Segmentum Command - Total War")
        self.resize(1200, 750)


    def init_ui(self):

        # Central widget
        central_widget = QWidget()
        self.setObjectName("central_widget")
        self.setCentralWidget(central_widget)

        # Main horizontal layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add widgets
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content, 1)