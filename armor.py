import sys, os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QLineEdit, QGroupBox

class ArmorWidget(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		hbox = QHBoxLayout()
		vbox = QVBoxLayout()
		
		self.head = ArmorItemWidget("Head","Helmet of Helmeting","1")
		self.torso = ArmorItemWidget("Torso","Breastplate of breastplating","1")
		self.arms = ArmorItemWidget("Arms","Gloves of gloving","1")
		self.legs = ArmorItemWidget("Legs","Pants of panting","1")
		self.feet = ArmorItemWidget("Feet","Boots of booting","1")
		
		vbox.addWidget(self.head)
		vbox.addWidget(self.torso)
		vbox.addWidget(self.arms)
		vbox.addWidget(self.legs)
		vbox.addWidget(self.feet)
		
		armor_guy = QLabel(self)
		armor_guy.setPixmap(QPixmap(resource_path("armor_guy.png")))
		hbox.addWidget(armor_guy)
		hbox.addLayout(vbox)
		self.setLayout(hbox)
		self.setFixedHeight(self.sizeHint().height())

class ArmorItemWidget(QGroupBox):
	
	def __init__(self,location,name,buff):
		super().__init__(location)
		self.name = name
		self.buff = buff
		self.initUI()
	
	def initUI(self):
		vbox = QVBoxLayout()
		self.armorItem = QLineEdit(self.name)
		self.buffField = QLineEdit(self.buff)
		vbox.addWidget(self.armorItem)
		vbox.addWidget(self.buffField)
		self.setLayout(vbox)
		 
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)