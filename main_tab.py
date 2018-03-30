from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLCDNumber, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSignal
import sys, os
import random

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
		
		self.levelbox.widgetUpdate.connect(player.updateStat)
		self.healthbox.widgetUpdate.connect(player.updateStat)
		self.strengthbox.widgetUpdate.connect(player.updateStat)
		
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
			
class StatWidget(QGroupBox):
	
	widgetUpdate=pyqtSignal(str,str)
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.statLine = QLineEdit(self.buff, self)
		self.validator = QIntValidator()
		self.statLine.setValidator(self.validator)
		self.rollButton = QPushButton("Roll", self)
		self.rollNumber = QLCDNumber(self)
		
		self.rollButton.clicked.connect(self.roll)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget(self.statLine)
		vbox.addWidget(self.rollButton)
		vbox.addWidget(self.rollNumber)
		self.setLayout(vbox)
		self.setFixedHeight(200)
		self.statLine.textChanged.connect(self.valUpdate)
	
	def valUpdate(self):
		self.widgetUpdate.emit(self.name,self.statLine.text())
		self.buff = self.statLine.text()
	
	def roll(self):
		self.rollNumber.display(random.randint(1,20 + int(self.buff)))

class LabelBoxWidget(QGroupBox):
	
	widgetUpdate=pyqtSignal(str,str)

	def __init__(self, name, value):
		self.name = name
		self.value = value
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.statLine = QLineEdit(str(self.value), self)
		self.validator = QIntValidator()
		self.statLine.setValidator(self.validator)
		vbox = QVBoxLayout()
		vbox.addWidget(self.statLine)
		self.setLayout(vbox)
		self.setFixedWidth(150)
		self.statLine.textChanged.connect(self.valUpdate)
	
	def valUpdate(self):
		self.widgetUpdate.emit(self.name,self.statLine.text())
		
class InventoryWidget(QGroupBox):

	widgetUpdate=pyqtSignal(str,int)

	def __init__(self, capacity, inventory):
		self.capacity = int(capacity)
		self.inventory = inventory
		super().__init__("Inventory")
		self.initUI()
		
	def initUI(self):
		list = QListWidget()
		vbox = QVBoxLayout()
		for i in range(len(self.inventory)):
			item = ListLineWidget(self.inventory[i],i)
			item.widgetUpdate.connect(self.valUpdate)
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		vbox.addWidget(list)
		self.setLayout(vbox)
	
	def valUpdate(self, name,index):
		self.widgetUpdate.emit(name,index)
		
class ListLineWidget(QLineEdit):
	
	widgetUpdate=pyqtSignal(str,int)

	
	def __init__(self, name, index):
		self.name=name
		self.index=index
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.textChanged.connect(self.valUpdate)
	
	def valUpdate(self, name):
		self.widgetUpdate.emit(name,self.index)
		
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)