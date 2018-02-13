from PyQt5.QtWidgets import QWidget, QVBoxLayout

class PlayerWidget(QWidget):

	def __init__(self, statFile):
		self.stats = parseStats(statFile)
		super().__init__()
		self.initUI()
		
	def initUI(self):
		hbox = QHBoxLayout(self)
		for stat in self.stats:
			for key, value in self.stats.iteritems():
				if(key=="CHARACTER_NAME"):
					self.strength=self.stats[key]
				else if(key=="PLAYER_NAME"):
					self.strength=self.stats[key]
				else if(key=="STRENGTH"):
					self.strength=self.stats[key]
				else if (key=="SIZE"):
					self.size=self.stats[key]
				else if (key=="CAPACITY"):
					self.capacity=self.stats[key]
				else if (key=="EXTRA_HEALTH"):
					self.extrahealth=self.stats[key]
				else:
					swidget = StatWidget(key,value)
					hbox.addWidget(swidget)
	
	def parseStats(file):
	stats = {};
	for line in file:
		if not line.startswith('#'):
			split = line.split('=')
			stats[split[0]]=split[1]
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