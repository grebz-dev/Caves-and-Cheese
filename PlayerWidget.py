from PyQt5.QtWidgets import QWidget QVBoxLayout

class PlayerWidget(QWidget):

	def __init__(self,stats):
		self.stats = stats
		super().__init__()
		self.initUI()
		
	def initUI(self):
	
		for stat in stats:
		
class StatWidget(QWidget):
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__()
		self.initUI()
		
	def initUI(self):
	
		groupbox = QGroupBox(self.name,self)
		statBox = QLineEdit(self)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget()
		
		