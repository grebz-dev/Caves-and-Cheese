from PyQt5.QtWidgets import QWidget, QVBoxLayout

class PlayerWidget(QWidget):

	def __init__(self, name, stats):
		self.stats = stats
		super().__init__()
		self.initUI()
		
	def initUI(self):
		for stat in self.stats:
			#iterate through stats dict and add widgets
	
	def parseStats(file):
	stats = {};
	for line in file:
		if not line.startswith('#'):
			split = line.split('=')
			stats[split[0]]=split[1]
	return stats
		
class StatWidget(QWidget):
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__()
		self.initUI()
		
	def initUI(self):
		statText = QLineEdit(self.buff, self)
		rollButton = QPushButton("Roll", self)
		display = QLCDNumber(self)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget(statText)
		vbox.addWidget(rollButton)
		vbox.addWidget(display)
		
		groupBox = QGroupBox(self.name,self)
		groupBox.addLayout(vbox)
		
		layout = QHBoxLayout(self)
		layout.addWidget(groupBox)
		
		self.setLayout(layout)