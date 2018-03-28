import sys
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget,QVBoxLayout,QPushButton
from main_tab import MainTabWidget
from notes import NotesWidget
from armor import ArmorWidget
from skills import SkillWidget

class MultiTabWidget(QWidget):
 
	def __init__(self, player):
		super().__init__()
		self.player = player
		self.initUI()

	def initUI(self):
		self.layout = QVBoxLayout(self)
		# Initialize tab screen
		self.tabs = QTabWidget()
		self.tab1 = QWidget()	
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()

		# Add items to populate tabs
		player = MainTabWidget(self.player)
		armor = ArmorWidget()
		notes = NotesWidget()
		skills = SkillWidget()
 
		# Add tabs
		self.tabs.addTab(self.tab1,"Player")
		self.tabs.addTab(self.tab2,"Armor")
		self.tabs.addTab(self.tab3,"Notes")
		self.tabs.addTab(self.tab4,"Skills")
 
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
			
		# Create third tab
		self.tab4.layout = QVBoxLayout(self)
		self.tab4.layout.addWidget(skills)
		self.tab4.setLayout(self.tab4.layout)

		# Add tabs to widget		
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)