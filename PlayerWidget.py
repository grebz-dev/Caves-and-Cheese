from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLCDNumber, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class PlayerWidget(QGroupBox):

	def __init__(self, statFile):
		self.stats = self.parseStats(statFile)
		self.health = 20
		self.initUI()
		
	def initUI(self):
		
		top_line = QHBoxLayout()
		bottom_line = QHBoxLayout()
		
		for key, value in self.stats.items():
			if(key=="CHARACTER_NAME"):
				self.character=self.stats[key]
			elif(key=="PLAYER_NAME"):
				self.player=self.stats[key]
			elif(key=="STRENGTH"):
				self.strength=self.stats[key]
			elif (key=="SIZE"):
				self.size=self.stats[key]
			elif (key=="CAPACITY"):
				self.capacity=self.stats[key]
			elif (key=="EXTRA_HEALTH"):
				self.health = self.health + int(self.stats[key])
			else:
				swidget = StatWidget(key,value)
				bottom_line.addWidget(swidget)
		super().__init__(self.character + " - " + self.player)
		
		stat_stack = QVBoxLayout()
		
		self.healthbox = LabelBoxWidget("Health",self.health)
		self.strengthbox = LabelBoxWidget("Strength",self.strength)
		self.sizebox = LabelBoxWidget("Size",self.size)
		
		stat_stack.addWidget(self.healthbox)
		stat_stack.addWidget(self.strengthbox)
		stat_stack.addWidget(self.sizebox)
		
		
		top_line.addLayout(stat_stack)
		
		top_line.addWidget(InventoryWidget(self.capacity))
		logo = QLabel(self)
		logo.setPixmap(QPixmap("logo-text.png"))
		top_line.addWidget(logo)
		
		vbox = QVBoxLayout()
		vbox.addLayout(top_line)
		vbox.addLayout(bottom_line)
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
		self.setFixedHeight(200)

class LabelBoxWidget(QGroupBox):
	
	def __init__(self, name, value):
		self.name = name
		self.value = value
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		statText = QLineEdit(str(self.value), self)
		vbox = QVBoxLayout()
		vbox.addWidget(statText)
		self.setLayout(vbox)
		self.setFixedWidth(150)
		
class InventoryWidget(QGroupBox):

	def __init__(self, capacity):
		self.capacity = int(capacity)
		super().__init__("Inventory")
		self.initUI()
	def initUI(self):
		list = QListWidget()
		vbox = QVBoxLayout()
		for i in range(self.capacity):
			item = QLineEdit()
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		vbox.addWidget(list)
		self.setLayout(vbox)