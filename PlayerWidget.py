from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLCDNumber

class PlayerWidget(QWidget):

	def __init__(self, statFile):
		self.stats = self.parseStats(statFile)
		super().__init__()
		self.initUI()
		
	def initUI(self):
		vbox = QVBoxLayout()
		
		hbox = QHBoxLayout()
		for key, value in self.stats.items():
			if(key=="CHARACTER_NAME"):
				self.strength=self.stats[key]
			elif(key=="PLAYER_NAME"):
				self.strength=self.stats[key]
			elif(key=="STRENGTH"):
				self.strength=self.stats[key]
			elif (key=="SIZE"):
				self.size=self.stats[key]
			elif (key=="CAPACITY"):
				self.capacity=self.stats[key]
			elif (key=="EXTRA_HEALTH"):
				self.extrahealth=self.stats[key]
			else:
				swidget = StatWidget(key,value)
				hbox.addWidget(swidget)
		vbox.addLayout(hbox)
		self.setLayout(vbox)
	
	def parseStats(self, file):
		stats = {}
		
		for line in file:
			if line and not line.startswith('#') and not line.startswith("\n"):
				split = line.split('=')
				stats[split[0]]=split[1].strip()
		return stats
		
class StatWidget(QGroupBox):
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		statText = QLineEdit(self.buff, self)
		rollButton = QPushButton("Roll", self)
		display = QLCDNumber(self)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget(statText)
		vbox.addWidget(rollButton)
		vbox.addWidget(display)
		
		self.setLayout(vbox)