from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

template ="""#Caves and Cheese player design form 

CHARACTER_NAME=
PLAYER_NAME=

#Distribute 40 points amongst ALL categories, including stats and fixed traits. If you
#don't want to assign a value, mark the field 0. DO NOT LEAVE VALUES BLANK

#Stats - boost rolls to determine actions
Range=
Magic=
Melee=
Defense=
Persuasion=
Healing=
Sneak=
Dexterity=
Crafting=


#Traits - score alone determines ability to perform actions
STRENGTH=
SIZE=
CAPACITY=
HEALTH=20
EXTRA_HEALTH=

#Items - The following are items that your character is carrying. Obviously, you cannot
#        carry more items than your CAPACITY would allow. Extra items will be truncated.
#        Each item MUST be preceded by a @ symbol, or else it will be parsed as a stat.
"""

def export(data, filename):
	tdata = data
	infile = open(filename)
	afile = open(filename,'a')
	for key, value in tdata.items():
		for line in infile:
			if line.split("=")[0] == key:
				line = key + "=" + value
			else:
				afile.write(key + "=" + value)

def save(data, filename):
	newTemplateFile(filename)
	export(data, filename)

def newTemplateFile(filename):
	file = open(filename,'a')
	file.write(template)
				
class SplashWidget(QWidget):
	
	fileOpened=pyqtSignal(str)

	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		
		vbox = QVBoxLayout(self)
		
		logo = QLabel(self)
		logo.setPixmap(QPixmap("splash.png"))
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
		filename, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if filename:
			self.fileOpened.emit(filename)
	
	def newTemplateDialog(self):
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			newTemplateFile(filename)