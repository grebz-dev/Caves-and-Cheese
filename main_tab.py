from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLCDNumber, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSignal
from main_tab_widgets import StatWidget, LabelBoxWidget,InventoryWidget
import sys, os

class MainTabWidget(QGroupBox):	

	def __init__(self, player):
		self.initUI(player)
		
	def initUI(self,player):
		
		top_line = QHBoxLayout()
		bottom_line = QHBoxLayout()
		
		for key, value in player.stats.items():
			swidget = StatWidget(key, value)
			bottom_line.addWidget(swidget)
			swidget.widgetUpdate.connect(player.updateStat)
		
		super().__init__(player.traits["CHARACTER_NAME"] + " - Size: " + player.traits["SIZE"] + " - " + player.traits["PLAYER_NAME"])
		
		
		stat_stack = QVBoxLayout()
		
		self.levelbox = LabelBoxWidget("Level",player.traits["LEVEL"])
		self.healthbox = LabelBoxWidget("Health",player.traits["HEALTH"])
		self.strengthbox = LabelBoxWidget("Strength",player.traits["STRENGTH"])
		
		self.levelbox.widgetUpdate.connect(player.updateTrait)
		self.healthbox.widgetUpdate.connect(player.updateTrait)
		self.strengthbox.widgetUpdate.connect(player.updateTrait)
		
		stat_stack.addWidget(self.levelbox)
		stat_stack.addWidget(self.healthbox)
		stat_stack.addWidget(self.strengthbox)
		
		top_line.addLayout(stat_stack)
				
		inventoryElement = InventoryWidget(player.traits["CAPACITY"],player.inventory)
		inventoryElement.widgetUpdate.connect(player.updateInventory)
		
		top_line.addWidget(inventoryElement)
		logo = QLabel(self)
		logo.setPixmap(QPixmap(resource_path("Images/logo-text.png")))
		top_line.addWidget(logo)
		
		vbox = QVBoxLayout()
		vbox.addLayout(top_line)
		vbox.addLayout(bottom_line)
		self.setLayout(vbox)

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)