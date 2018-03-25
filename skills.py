from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from Player import ListLineWidget


class SkillWidget():

	widgetUpdate=pyqtSignal(str,int)

	def __init__(self, items):
		self.capacity = int(capacity)
		self.items = items
		self.capacity=20
		super().__init__()
		self.initUI()
		
	def initUI(self):
		list = QListWidget()
		vbox = QVBoxLayout()
		for i in range(self.capacity):
			item = ListLineWidget(self.items[i],i)
			item.widgetUpdate.connect(self.valUpdate)
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		vbox.addWidget(list)
		self.setLayout(vbox)
	
	def valUpdate(self, name,index):
		self.widgetUpdate.emit(name,index)