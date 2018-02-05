from PyQt5.QtWidgets import QWidget

class PlayerWidget(QWidget):

	def __init__(self,stats):
		self.stats = stats
		super().__init__()
		self.initUI()
		
	def initUI(self):
	
		for stat in stats:
		
# class StatWidget(QWidget):
	
	def __init__(self, statName, statValue):
		self.statName = statName
		self.statValue = statValue
		super().__init__()
		self.initUI()
		
	def initUI(self):
		