from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
import requests
from PySide6.QtGui import QPixmap, QMovie

class PokeWindow(QWidget):
     def __init__(self):
        super().__init__()