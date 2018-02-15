from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton

def export(data, file):
	tdata = data
	for key, value in tdata.items():
		for line in file:
			if line.split("=")[0] == key:
				line = key + "=" + value
			else:
				file.append(key + "=" + value)
				
class SplashWidget(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		
		vbox = QVBoxLayout(self)
		
		logo = QLabel(self)
		logo.setPixmap(QPixmap("logo-text.png"))
		vbox.addWidget(logo)
		
		hbox = QHBoxLayout(self)
		hbox.addStretch()
		open_button = QPushButton(self, "Open Character")
		new_button = QPushButton(self, "New Empty Character Template")
		exit_button = QPushButton(self, "Exit Caves and Cheese")
		hbox.addWidget(open_button)
		hbox.addWidget(new_button)
		hbox.addWidget(exit_button)
		
		vbox.addLayout(hbox)
		self.setLayout(vbox)