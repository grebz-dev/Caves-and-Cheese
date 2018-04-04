from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
import sys, os
from main_tab_widgets import LabelBoxWidget
				
class SplashWidget(QWidget):
	
	start=pyqtSignal(str)

	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		
		vbox = QVBoxLayout(self)
		top_hbox = QHBoxLayout(self)
		
		logo = QLabel(self)
		logo.setPixmap(QPixmap(resource_path("Images/splash.png")))
		top_hbox.addWidget(logo)

		self.character_name = LabelBoxWidget("New Character Name","")
		self.player_name = LabelBoxWidget("New Player Name","")
		self.size = LabelBoxWidget("New Character Size")
		top_hbox.addwidget(self.player_name)
		top_hbox.addWidget(self.character_name)
		top_hbox.addWidget(self.size)
		
		vbox.addLayout(top_hbox)
		
		bottom_hbox = QHBoxLayout(self)
		bottom_hbox.addStretch()
		self.open_button = QPushButton("Open Character")
		self.new_button = QPushButton("New Character")
		
		self.open_button.clicked.connect(self.openDialog)
		self.new_button.clicked.connect(self.newCharacter)
		
		bottom_hbox.addWidget(self.open_button)
		bottom_hbox.addWidget(self.new_button)
		
		vbox.addLayout(bottom_hbox)
		self.setLayout(vbox)
	
	def openDialog(self):    
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			self.start.emit(pickle.load(open(filename, "rb" )))
			
	def newCharacter(self):
		
		self.start.emit(Player())

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)