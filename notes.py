from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPlainTextEdit


class NotesWidget(QWidget):

	def __init__(self):
			super().__init__()
			self.initUI()
		
	def initUI(self):
		layout = QVBoxLayout()
		textedit = QPlainTextEdit()
		layout.addWidget(textedit)
		self.setLayout(layout)