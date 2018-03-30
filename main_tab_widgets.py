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
		for i in range(len(self.inventory)):
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
		