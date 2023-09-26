
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QMessageBox
import requests
from PySide6.QtGui import QPixmap, QMovie, QImage
from api import poke_data, get_pokename, get_poke_abilities, get_poke_type, get_pokestats, get_poke_img, download_image
from poke_window import PokeWindow
from display_window import DisplayWindow
import json


class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 850, 500) 

        background_image = QPixmap("../assets/landing.png")  
        self.background_label.setPixmap(background_image)

      
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        self.w = None        
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        
        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.open_poke_window)
        
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.open_alert_window)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.open_display_window)

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.


    def open_poke_window(self, checked):
        
        if self.w is None:
            print('a')
            self.w = PokeWindow(self)
        self.w.show()

    def open_alert_window(self):
         instance = PokeWindow(self)
         url = instance.pic
         download_image(url, instance.pokename)
         msgBox = QMessageBox()
         msgBox.setText("Pokemon Successfully captured.")
         msgBox.exec_()
 
    def open_display_window(self):
        print("b")
        self.w = DisplayWindow(self)
        self.w.show()

    
  








