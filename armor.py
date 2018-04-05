import sys, os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QLineEdit, QGroupBox

class ArmorWidget(QWidget):
	
	def __init__(self, player):
		super().__init__()
		self.initUI(player)
	
	def initUI(self, player):
		hbox = QHBoxLayout()
		vbox = QVBoxLayout()
		
		for key, value in player.armor.items():
			widget = ArmorItemWidget(key,value[0],value[1])
			widget.armorItem.textChanged.connect(lambda location, item, buff, player=player : self.valUpdate(location, item, buff, player))
			vbox.addWidget(widget)
		
		armor_guy = QLabel(self)
		armor_guy.setPixmap(QPixmap(resource_path("Images/armor_guy.png")))
		hbox.addWidget(armor_guy)
		hbox.addLayout(vbox)
		self.setLayout(hbox)
		self.setFixedHeight(self.sizeHint().height())
		
		def valUpdate(self, location, item, buff, player):
			player.updateArmor(location, item, buff)

class ArmorItemWidget(QGroupBox):

	widgetUpdate=pyqtSignal(str,str,str)
	
	def __init__(self,location,name,buff):
		super().__init__(location)
		self.location = location
		self.name = name
		self.buff = buff
		self.initUI()
	
	def initUI(self):
		vbox = QVBoxLayout()
		self.armorItem = QLineEdit(self.name)
		self.armorItem.setPlaceholderText("Enter name of item")
		self.buffField = QLineEdit(self.buff)
		self.buffField.setPlaceholderText("Enter item buff or quality")
		vbox.addWidget(self.armorItem)
		vbox.addWidget(self.buffField)
		self.setLayout(vbox)
		
	def valUpdate(self):
		self.buff = self.buffField.text()
		self.name = self.armorItem.text()
		self.widgetUpdate.emit(self.location,self.name, self.buff)
		 
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)