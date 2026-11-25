from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from components.ship_database.ship_list_panel import ShipListPanel
from components.ship_database.ship_dossier_panel import ShipDossierPanel

class ShipDatabase(QWidget):
    def __init__(self):
            super().__init__()
            self.setObjectName("ship_database")
    
            self.init_ui()
            #self.init_connections()

    def init_ui(self):
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(15, 20, 15, 20)
        self.main_layout.setSpacing(10)

        self.ship_list = ShipListPanel()
        self.ship_dossier = ShipDossierPanel()

        # Add both panels to the layout
        # Placeholder for layout code

        self.main_layout.addWidget(self.ship_list)
        self.main_layout.addWidget(self.ship_dossier)

        # 30% left, 70% right
        self.main_layout.setStretch(0, 3)
        self.main_layout.setStretch(1, 7)

    """
    def init_connections(self):
        self.ship_list.ship_selected.connect(
            self.ship_dossier.set_ship
        )
    """