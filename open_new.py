from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
import sys, os

template ="""#Caves and Cheese player design form 

CHARACTER_NAME=
PLAYER_NAME=
SIZE=

#Distribute 50 points amongst ALL categories, including stats and fixed traits. If you
#don't want to assign a value, mark the field 0. DO NOT LEAVE VALUES BLANK

#Stats - boost rolls to determine actions
Range=
Magic=
Melee=
Defense=
Charisma=
Healing=
Dexterity=
Intelligence=


#Traits - score alone determines ability to perform actions
STRENGTH=
EXTRA_HEALTH=
CAPACITY=

#Set by default
HEALTH=20
LEVEL=1

#Items - The following are items that your character is carrying. Obviously, you cannot
#        carry more items than your CAPACITY would allow. Extra items will be truncated.
#        Each item MUST be preceded by a @ symbol, or else it will be parsed as a stat.

@Rope
@Provisions (heals +5) x2
@Hunting Knife (Damage cap 5)
@Flint and Striker
@Small hatchet (Damage cap 3)
@Gold
"""

def newTemplateFile(filename):
	file = open(filename,'w+')
	file.write(template)
				
class SplashWidget(QWidget):
	
	fileOpened=pyqtSignal(str)

	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		
		vbox = QVBoxLayout(self)
		
		logo = QLabel(self)
		logo.setPixmap(QPixmap(resource_path("splash.png")))
		vbox.addWidget(logo)
		
		hbox = QHBoxLayout(self)
		hbox.addStretch()
		self.open_button = QPushButton("Open Character")
		self.new_button = QPushButton("New Empty Character Template")
		
		self.open_button.clicked.connect(self.openDialog)
		self.new_button.clicked.connect(self.newTemplateDialog)
		
		hbox.addWidget(self.open_button)
		hbox.addWidget(self.new_button)
		
		vbox.addLayout(hbox)
		self.setLayout(vbox)
	
	def openDialog(self):    
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			self.fileOpened.emit(filename)
	
	def newTemplateDialog(self):
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			newTemplateFile(filename)

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)