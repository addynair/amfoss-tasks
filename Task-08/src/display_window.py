from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import  QRect
import os
import requests
from PySide6.QtGui import QPixmap, QImage

class DisplayWindow(QWidget):
    def __init__(self,search_window_class):
        super().__init__()

        self.filenames = []
        self.setFixedSize(650,500)
        self.current_index = 0
        
        self.dir_path = r'./images'
        list = []
        

        for file_path in os.listdir(self.dir_path):
            if os.path.isfile(os.path.join(self.dir_path, file_path)):
                list.append(file_path)
        
        # self.filenames = list
        

        self.label_pic = QLabel(self)
            
        pixmap = QPixmap("images/{}".format(list[0]))
        self.label_pic.setPixmap(pixmap)
        
        

        previous_button = QPushButton("Previous",self)
        previous_button.setGeometry(180,460,80,30)

        next_button = QPushButton("Next",self)
        next_button.setGeometry(500,460,80,30)

        previous_button.clicked.connect(self.handle_previous)
        next_button.clicked.connect(self.handle_next)
        self.load_files()
    
    def load_files(self):
        self.filenames = os.listdir(self.dir_path)
        print(self.filenames)


    @property
    def current_index(self):
        return self.current_index

    @current_index.setter
    def current_index(self, index):
        
        print("length is",len(self.filenames))
        if 0 <= index < len(self.filenames):
            self.current_index = index
            filename = self.filenames[self.current_index]
            pixmap = QPixmap("images/{}".format(filename))
            self.label_pic.setPixmap(pixmap)

    
    def __len__(self):
        return len(self.filenames)

    def handle_next(self):
        self.current_index += 1
        print(self.current_index)

    def handle_previous(self):
        self.current_index -= 1  
        print(self.current_index)  
    
   
