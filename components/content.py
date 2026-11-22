from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QLabel

class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("content")

        self.init_pages()

    def init_pages(self):
        pages = [
            "Dashboard",
            "Ship Constructor",
            "Ship Database",
            "Factions",
            "Fleet Builder",
            "Lua Exporter",
        ]

        for page_name in pages:
            page = PlaceholderPage(page_name)
            self.addWidget(page)

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