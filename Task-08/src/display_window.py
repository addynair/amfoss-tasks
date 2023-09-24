from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import  QRect
import os
import requests
from PySide6.QtGui import QPixmap, QImage

class DisplayWindow(QWidget):
    def __init__(self,search_window_class):
        super().__init__()


        self.setFixedSize(450, 200)
        
        dir_path = r'./images'
        list = []
        for file_path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, file_path)):
                list.append(file_path)
        
        
        self._current_index = 0
        self._filenames = []

        self.previous_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")

        self.label = QLabel()

        lay = QGridLayout(self)
        lay.addWidget(self.previous_button, 0, 0)
        lay.addWidget(self.next_button, 0, 1)
        lay.addWidget(self.label, 1, 0, 1, 3)

        self.previous_button.clicked.connect(self.handle_previous)
        self.next_button.clicked.connect(self.handle_next)
        self.load_files()


    # @property
    # def current_index(self):
    #     return self._current_index

    # @current_index.setter
    # def current_index(self, index):

    #     if 0 <= index < __len__(self):
    #         self._current_index = index
    #         filename = self._filenames[self._current_index]
    #         pixmap = QPixmap(filename)
    #         self.label.setPixmap(pixmap)


    def load_files(self):
        self._filenames = list
        
        self.current_index = 0

    
    def __len__(self):
        return len(self._filenames)

    def handle_next(self):
        self.current_index += 1

    def handle_previous(self):
        self.current_index -= 1    
    
   
