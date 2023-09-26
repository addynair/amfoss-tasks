from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import  QRect
import os
import requests
from PySide6.QtGui import QPixmap, QImage

class DisplayWindow(QWidget):
    def __init__(self, search_window_class):
        super().__init__()

        self.filenames = []
        self.setFixedSize(650, 500)
        self.index = 0
        self.dir_path = r'./images'
        self.load_files()

        previous_button = QPushButton("Previous", self)
        previous_button.setGeometry(100, 460, 80, 30)

        next_button = QPushButton("Next", self)
        next_button.setGeometry(500, 460, 80, 30)

        previous_button.clicked.connect(self.handle_previous)
        next_button.clicked.connect(self.handle_next)

        self.label_pic = QLabel(self)
        self.load_pic(self.index)

    def load_files(self):
        for file_path in os.listdir(self.dir_path):
            if os.path.isfile(os.path.join(self.dir_path, file_path)):
                self.filenames.append(file_path)

    def load_pic(self, index):
        if 0 <= index < len(self.filenames):
            filename = self.filenames[index]
            pixmap = QPixmap("./images/{}".format(filename))
            self.label_pic.setPixmap(pixmap)

    def handle_next(self):
        self.index += 1
        self.load_pic(self.index)

    def handle_previous(self):
        self.index -= 1
        self.load_pic(self.index)
