from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
import sys, os
from main_tab_widgets import LabelBoxWidget
from player import Player
				
class SplashWidget(QWidget):
	
	start=pyqtSignal(Player)

	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		hbox = QHBoxLayout(self)
		
		logo = QLabel(self)
		logo.setPixmap(QPixmap(resource_path("Images/splash.png")))
		hbox.addWidget(logo)

		vbox = QVBoxLayout()
		hbox.addLayout(vbox)
		
		self.character_name = LabelBoxWidget("New Character Name","")
		self.player_name = LabelBoxWidget("New Player Name","")
		self.size = LabelBoxWidget("New Character Size","")
		vbox.addWidget(self.player_name)
		vbox.addWidget(self.character_name)
		vbox.addWidget(self.size)
		
		
		self.open_button = QPushButton("Open Character")
		self.new_button = QPushButton("New Character")
		
		self.open_button.clicked.connect(self.openDialog)
		self.new_button.clicked.connect(self.newCharacter)
		
		button_hbox = QHBoxLayout()
		button_hbox.addWidget(self.open_button)
		button_hbox.addWidget(self.new_button)
		vbox.addLayout(button_hbox)
		
		
			
	def openDialog(self):    
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			self.start.emit(pickle.load(open(filename, "rb" )))
			
	def newCharacter(self):
		player = Player()
		player.init_new(self.character_name.value,self.player_name.value,self.size.value)
		self.start.emit(player)

def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)