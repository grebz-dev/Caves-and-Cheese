from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from main_tab import ListLineWidget


class SkillWidget(QWidget):

	widgetUpdate=pyqtSignal(str,int)

	def __init__(self, skills):
		self.skills = skills
		self.size=20
		super().__init__()
		self.initUI()
		
	def initUI(self):
		list = QListWidget()
		vbox = QVBoxLayout()
		for i in range(self.size):
			item = ListLineWidget("",i)
			item.widgetUpdate.connect(self.valUpdate)
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		for i in range (len(self.skills)):
			self.valUpdate(self.skills[i],i)
		vbox.addWidget(list)
		self.setLayout(vbox)
	
	def valUpdate(self, name,index):
		self.widgetUpdate.emit(name,index)