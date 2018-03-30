from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from main_tab import ListLineWidget


class SkillWidget(QWidget):

	widgetUpdate=pyqtSignal(str,int)

	def __init__(self, player):
		super().__init__()
		self.initUI()
		
	def initUI(self, player):
		list = QListWidget()
		vbox = QVBoxLayout()
		
		while len(player.skills) < 20:
			player.skills.append("")
		
		for i in range(len(player.skills)):
			item = ListLineWidget(player.skills[i],i)
			item.widgetUpdate.connect(self.valUpdate)
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
			
		vbox.addWidget(list)
		self.setLayout(vbox)
	
	def valUpdate(self, name, index):
		self.widgetUpdate.emit(name,index)