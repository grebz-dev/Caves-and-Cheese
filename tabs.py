import sys
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget,QVBoxLayout
from Player import PlayerWidget
from armor import ArmorWidget

class MultiTabWidget(QWidget):
 
    def __init__(self, statFile):
        super().__init__()
        self.statFile = statFile
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()

        # Add items to populate tabs
        player = PlayerWidget(self.statFile)
        armor = ArmorWidget()
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Player")
        self.tabs.addTab(self.tab2,"Armor")
 
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(player)
        
        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(armor)
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)