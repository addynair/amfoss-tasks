
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QMessageBox
import requests
from PySide6.QtGui import QPixmap, QMovie, QImage
from api import poke_data, get_pokename, get_poke_abilities, get_poke_type, get_pokestats, get_poke_img
from poke_window import PokeWindow
import json


class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
       
        # self.textbox.setStyleSheet("""position: absolute""" )

       
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
        # label1.setStyleSheet("""
        #                       background-color: grey
        #                       postion: relative
        #                       """)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.open_poke_window)
        
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.open_alert_window)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        # display_button.clicked.connect(self.open_display_window)

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.
    
    # def get_text(self):
    #     poke_name = self.textbox.text()
    #     print(poke_name)
    #     return poke_name



     
    def open_poke_window(self, checked):

        # name_label = QLabel("Name: ",self)  
        # name_label.setGeometry(50, 0, 600, 70)

        # data = poke_data(self.textbox.text())


        # name = QLabel(get_pokename(data),self)  
        # name.setGeometry(200, 10, 200, 70)

        # ability_label = QLabel("Ability: ",self) 
        # ability_label.setGeometry(10, 20, 600, 70)

        # ability = QLabel(' '.join(get_poke_abilities(data)),self) 
        # ability.setGeometry(170, 20, 600, 70)
        

        # type_label = QLabel("Types: ",self) 
        # type_label.setGeometry(50, 40, 600, 70)

        # type = QLabel(get_poke_type(data),self) 
        # type.setGeometry(170, 40, 600, 70)

        # stats_label = QLabel("Stats: ",self)   
        # stats_label.setGeometry(50, 60, 600, 70)
        
        # poke_stats = get_pokestats(data)
        

        # hp_label = QLabel("hp: ",self) 
        # hp_label.setGeometry(50, 80, 600, 70)
        
        # hp = QLabel(str(poke_stats['hp']),self) 
        # hp.setGeometry(170, 80, 600, 70)

        # attack_label = QLabel("attack: ",self) 
        # attack_label.setGeometry(50, 100, 600, 70)

        # attack = QLabel(str(poke_stats['attack']),self) 
        # attack.setGeometry(170, 100, 600, 70)

        # defense_label = QLabel("defense: ",self) 
        # defense_label.setGeometry(50, 120, 600, 70)

        # defense = QLabel(str(poke_stats['defense']),self) 
        # defense.setGeometry(170, 120, 600, 70)

        # special_attack_label = QLabel("special-attack: ",self) 
        # special_attack_label.setGeometry(50, 140, 600, 70)

        # special_attack = QLabel(str(poke_stats['special-attack']),self) 
        # special_attack.setGeometry(170, 140, 600, 70)

        # special_defense_label = QLabel("special-defense: ",self)
        # special_defense_label.setGeometry(50, 160, 600, 70)

        # special_defense = QLabel(str(poke_stats['special-defense']),self)
        # special_defense.setGeometry(170, 160, 600, 70)

        # speed_label = QLabel("speed: ",self) 
        # speed_label.setGeometry(50, 180, 600, 70)

        # speed = QLabel(str(poke_stats['speed']),self) 
        # speed.setGeometry(170, 180, 600, 70)

        # pic = get_poke_img(data)
        # image = QImage()
        # image.loadFromData(requests.get(pic).content)
        # self.background_label.setStyleSheet("""background-image: dark-grey;""")
         
         
         
         
        
        if self.w is None:
            self.w = PokeWindow(self)
        self.w.show()

    def open_alert_window(self):
         print(PokeWindow.pic)
         msgBox = QMessageBox()
         msgBox.setText("Pokemon Successfully captured.")
         msgBox.exec_()
 
    
  








