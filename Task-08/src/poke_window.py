from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import  QRect
import requests
from PySide6.QtGui import QPixmap, QImage
from api import poke_data, get_pokename, get_poke_abilities, get_poke_type, get_pokestats, get_poke_img




class PokeWindow(QWidget):
     def __init__(self,search_window_class):
        super().__init__()
        self.pokename = search_window_class.textbox.text()
        data = poke_data(self.pokename)

        self.pic = get_poke_img(data)
        image = QImage()
        image.loadFromData(requests.get(self.pic).content)
        label = QLabel(self)
        pixmap = QPixmap(image)
        label.setPixmap(pixmap)
        label.setGeometry(QRect(250, 0, 500,500))
        
        name_label = QLabel("Name: ",self)  
        name_label.setGeometry(50, 0, 600, 70)

        name = QLabel(get_pokename(data),self)  
        name.setGeometry(170, 0, 600, 70)

        ability_label = QLabel("Ability: ",self) 
        ability_label.setGeometry(50, 20, 600, 70)

        ability = QLabel(' '.join(get_poke_abilities(data)),self) 
        ability.setGeometry(170, 20, 600, 70)
        

        type_label = QLabel("Types: ",self) 
        type_label.setGeometry(50, 40, 600, 70)

        type = QLabel(get_poke_type(data),self) 
        type.setGeometry(170, 40, 600, 70)

        stats_label = QLabel("Stats: ",self)   
        stats_label.setGeometry(50, 60, 600, 70)
        
        poke_stats = get_pokestats(data)
        

        hp_label = QLabel("hp: ",self) 
        hp_label.setGeometry(50, 80, 600, 70)
        
        hp = QLabel(str(poke_stats['hp']),self) 
        hp.setGeometry(170, 80, 600, 70)

        attack_label = QLabel("attack: ",self) 
        attack_label.setGeometry(50, 100, 600, 70)

        attack = QLabel(str(poke_stats['attack']),self) 
        attack.setGeometry(170, 100, 600, 70)

        defense_label = QLabel("defense: ",self) 
        defense_label.setGeometry(50, 120, 600, 70)

        defense = QLabel(str(poke_stats['defense']),self) 
        defense.setGeometry(170, 120, 600, 70)

        special_attack_label = QLabel("special-attack: ",self) 
        special_attack_label.setGeometry(50, 140, 600, 70)

        special_attack = QLabel(str(poke_stats['special-attack']),self) 
        special_attack.setGeometry(170, 140, 600, 70)

        special_defense_label = QLabel("special-defense: ",self)
        special_defense_label.setGeometry(50, 160, 600, 70)

        special_defense = QLabel(str(poke_stats['special-defense']),self)
        special_defense.setGeometry(170, 160, 600, 70)

        speed_label = QLabel("speed: ",self) 
        speed_label.setGeometry(50, 180, 600, 70)

        speed = QLabel(str(poke_stats['speed']),self) 
        speed.setGeometry(170, 180, 600, 70)
         
         
         
         
        