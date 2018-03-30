from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit


class NotesWidget(QWidget):

	def __init__(self,player):
			super().__init__()
			self.initUI(player)
		
	def initUI(self, player):
		layout = QVBoxLayout()
		textedit = QPlainTextEdit()

		textedit.textChanged.connect(self.valUpdate)
		layout.addWidget(textedit)
		self.setLayout(layout)
		
	def valUpdate(self):
		self.widgetUpdate.emit()