import random
import sys, os

class Player(QGroupBox):	

	def __init__(self, statFile):
		self.inventory = []
		self.stats = {}
		self.notes = {}
		self.skills = {}
		self.health = 20
		self.parseStats(statFile)
		self.initUI()
		
	def updateStat(self, key, value):
		self.stats[key]=value
		print(self.stats)
		
	def updateInventory(self, item, index):
		self.inventory[index]=item
		print(self.inventory)
	
	def parseStats(self, filename):
		file = open(filename)
		for line in file:
			if line and not line.startswith('#') and not line.startswith("\n"):
				if line.startswith('@'):
					self.inventory.append(line[1:].strip())
				if line.startswith('^'):
					self.skills.append(line[1:].strip())
				if line.startswith('?'):
					self.notes.append(line[1:].strip())
				else:
					split = line.split('=')
					self.stats[split[0]]=split[1].strip()
	
	def saveDialog(self):
		options = QFileDialog.Options()
		filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","Caves and Cheese Files (*.cnc)", options=options)
		if filename:
			self.export(filename)
	
	def export(self, filename):
		file = open(filename,'w+')
		
		for key, value in self.stats.items():
			file.write(key+"="+str(value)+"\n")
		
		for item in self.inventory:
			if not item == "":
				file.write('@'+item+"\n")
			
class StatWidget(QGroupBox):
	
	widgetUpdate=pyqtSignal(str,str)
	
	def __init__(self, name, buff):
		self.name = name
		self.buff = buff
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.statLine = QLineEdit(self.buff, self)
		self.validator = QIntValidator()
		self.statLine.setValidator(self.validator)
		self.rollButton = QPushButton("Roll", self)
		self.rollNumber = QLCDNumber(self)
		
		self.rollButton.clicked.connect(self.roll)
		
		vbox = QVBoxLayout(self)
		vbox.addWidget(self.statLine)
		vbox.addWidget(self.rollButton)
		vbox.addWidget(self.rollNumber)
		self.setLayout(vbox)
		self.setFixedHeight(200)
		self.statLine.textChanged.connect(self.valUpdate)
	
	def valUpdate(self):
		self.widgetUpdate.emit(self.name,self.statLine.text())
		self.buff = self.statLine.text()
	
	def roll(self):
		self.rollNumber.display(random.randint(1,20 + int(self.buff)))

class LabelBoxWidget(QGroupBox):
	
	widgetUpdate=pyqtSignal(str,str)

	def __init__(self, name, value):
		self.name = name
		self.value = value
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.statLine = QLineEdit(str(self.value), self)
		self.validator = QIntValidator()
		self.statLine.setValidator(self.validator)
		vbox = QVBoxLayout()
		vbox.addWidget(self.statLine)
		self.setLayout(vbox)
		self.setFixedWidth(150)
		self.statLine.textChanged.connect(self.valUpdate)
	
	def valUpdate(self):
		self.widgetUpdate.emit(self.name,self.statLine.text())
		
class InventoryWidget(QGroupBox):

	widgetUpdate=pyqtSignal(str,int)

	def __init__(self, capacity, inventory):
		self.capacity = int(capacity)
		self.inventory = inventory
		super().__init__("Inventory")
		self.initUI()
		
	def initUI(self):
		list = QListWidget()
		vbox = QVBoxLayout()
		for i in range(self.capacity):
			item = ListLineWidget(self.inventory[i],i)
			item.widgetUpdate.connect(self.valUpdate)
			listWidgetItem = QListWidgetItem(list)
			list.addItem(listWidgetItem)
			list.setItemWidget(listWidgetItem, item)
		vbox.addWidget(list)
		self.setLayout(vbox)
	
	def valUpdate(self, name,index):
		self.widgetUpdate.emit(name,index)
		
class ListLineWidget(QLineEdit):
	
	widgetUpdate=pyqtSignal(str,int)

	
	def __init__(self, name, index):
		self.name=name
		self.index=index
		super().__init__(name)
		self.initUI()
		
	def initUI(self):
		self.textChanged.connect(self.valUpdate)
	
	def valUpdate(self, name):
		self.widgetUpdate.emit(name,self.index)
		
def resource_path(relative_path):
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, relative_path)
	return os.path.join(os.path.abspath("."), relative_path)