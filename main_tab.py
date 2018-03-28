from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLCDNumber, QListWidget, QListWidgetItem, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSignal
import sys, os
import random

class MainTabWidget(QGroupBox):	

	def __init__(self, player):
		self.player = player
		self.initUI()
		
	def initUI(self):
		
		top_line = QHBoxLayout()
		bottom_line = QHBoxLayout()
		
		for key, value in self.player.stats.items():
			swidget = StatWidget(key, value)
			bottom_line.addWidget(swidget)
			swidget.widgetUpdate.connect(self.player.updateStat)
		
		super().__init__(self.player.traits["CHARACTER_NAME"] + " - Size: " + self.player.traits["SIZE"] + " - " + self.player.traits["PLAYER_NAME"])
		
		
		stat_stack = QVBoxLayout()
		
		self.levelbox = LabelBoxWidget("Level",self.player.traits["LEVEL"])
		self.healthbox = LabelBoxWidget("Health",self.player.traits["HEALTH"])
		self.strengthbox = LabelBoxWidget("Strength",self.player.traits["STRENGTH"])
		
		self.levelbox.widgetUpdate.connect(self.player.updateStat)
		self.healthbox.widgetUpdate.connect(self.player.updateStat)
		self.strengthbox.widgetUpdate.connect(self.player.updateStat)
		
		stat_stack.addWidget(self.levelbox)
		stat_stack.addWidget(self.healthbox)
		stat_stack.addWidget(self.strengthbox)
		
		save_stack = QVBoxLayout()
		top_line.addLayout(stat_stack)
		
		self.save_button = QPushButton("Save Character")
		self.save_button.setFixedWidth(200)
		self.save_button.clicked.connect(self.saveDialog)
		self.save_button_layout = QHBoxLayout()
		self.save_button_layout.addWidget(self.save_button)
		
		save_stack.addLayout(self.save_button_layout)
		
		inventoryElement = InventoryWidget(self.player.traits["CAPACITY"],self.player.inventory)
		inventoryElement.widgetUpdate.connect(self.player.updateInventory)
		
		top_line.addWidget(inventoryElement)
		logo = QLabel(self)
		logo.setPixmap(QPixmap(resource_path("Images/logo-text.png")))
		save_stack.addWidget(logo)

		
		top_line.addLayout(save_stack)
		
		vbox = QVBoxLayout()
		vbox.addLayout(top_line)
		vbox.addLayout(bottom_line)
		self.setLayout(vbox)
	
	def saveDialog(self):
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			self.export(filename)
			
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
		for i in range(self.capacity):
			item = ListLineWidget("",i)
			item.widgetUpdate.connect(self.valUpdate)
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		for i in range (len(self.inventory)):
			self.valUpdate(self.inventory[i],i)
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