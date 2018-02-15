from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

def export(data, file):
	tdata = data
	for key, value in tdata.items():
		for line in file:
			if line.split("=")[0] == key:
				line = key + "=" + value
			else:
				file.append(key + "=" + value)
				
class SplashWidget(QWidget):
	fileName = ''
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
		new_button = QPushButton("New Empty Character Template")
		exit_button = QPushButton("Exit Caves and Cheese")
		
		self.open_button.clicked.connect(self.openDialog)
		
		hbox.addWidget(self.open_button)
		hbox.addWidget(new_button)
		hbox.addWidget(exit_button)
		
		
		vbox.addLayout(hbox)
		self.setLayout(vbox)
	
	def setFileName(self, name):
		self.fileName=name
	
	def openDialog(self):    
		options = QFileDialog.Options()
		fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			self.fileName = fileName