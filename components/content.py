from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QLabel
from pages.ship_database import ShipDatabase

class PlaceholderPage(QWidget):

    def __init__(self, page_name):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel(page_name)
        title.setObjectName("pageTitle")

        subtitle = QLabel("This section is under construction.")
        subtitle.setObjectName("subtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()

class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("content")

        self.init_pages()

    def init_pages(self):
        pages = [
            ("Dashboard", PlaceholderPage("Dashboard")),
            ("Ship Constructor", PlaceholderPage("Ship Constructor")),
            ("Ship Database", ShipDatabase()),
            ("Factions", PlaceholderPage("Factions")),
            ("Fleet Builder", PlaceholderPage("Fleet Builder")),
            ("Lua Exporter", PlaceholderPage("Lua Exporter")),
        ]

        for page_name, page in pages:
            self.addWidget(page)