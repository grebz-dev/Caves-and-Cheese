from PyQt5.QtWidgets import QWidget

class PlayerWidget(QWidget):

	def __init__(self,parent,stats):
		self.stats = stats
		super().__init__()
		self.initUI()
		
	def initUI(self):
	
		for stat in stats:
		
class StatWidget(QWidget):