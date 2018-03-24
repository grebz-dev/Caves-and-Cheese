import sys
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget,QVBoxLayout,QPushButton
from Player import PlayerWidget
from notes import NotesWidget
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
		self.tab3 = QWidget()

		# Add items to populate tabs
		player = PlayerWidget(self.statFile)
		armor = ArmorWidget()
		notes = NotesWidget()
 
		# Add tabs
		self.tabs.addTab(self.tab1,"Player")
		self.tabs.addTab(self.tab2,"Armor")
		self.tabs.addTab(self.tab3,"Notes")
 
		# Create first tab
		self.tab1.layout = QVBoxLayout(self)
		self.tab1.layout.addWidget(player)
		self.tab1.setLayout(self.tab1.layout)
		
		# Create second tab
		self.tab2.layout = QVBoxLayout(self)
		self.tab2.layout.addWidget(armor)
		self.tab2.setLayout(self.tab2.layout)
		
		# Create third tab
		self.tab3.layout = QVBoxLayout(self)
		self.tab3.layout.addWidget(notes)
		self.tab3.setLayout(self.tab3.layout)

		# Add tabs to widget		
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)