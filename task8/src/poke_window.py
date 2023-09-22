from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
import requests
from PySide6.QtGui import QPixmap, QMovie
from api import poke_data, get_pokename, get_poke_abilities, get_poke_type, get_pokestats




class PokeWindow(QWidget):
     def __init__(self,search_window_class):
        super().__init__()
        pokename = search_window_class.textbox.text()
        data = poke_data(pokename)
        print(get_poke_abilities(data))
        
        

        name_label = QLabel("Name: ",self)  
        name_label.setGeometry(50, 10, 600, 70)

        name = QLabel(get_pokename(data),self)  
        name.setGeometry(120, 10, 600, 70)

        ability_label = QLabel("Ability: ",self) 
        ability_label.setGeometry(50, 15, 600, 70)

        ability = QLabel(' '.join(get_poke_abilities(data)),self) 
        ability.setGeometry(120, 15, 600, 70)
        

        type_label = QLabel("Types: ",self) 
        type_label.setGeometry(50, 40, 600, 70)

        type = QLabel(get_poke_type(data),self) 
        type.setGeometry(120, 40, 600, 70)

        stats_label = QLabel("Stats: ",self)   
        stats_label.setGeometry(50, 60, 600, 70)
        
        poke_stats = get_pokestats(data)
        # stats = QLabel(' '.join(get_pokestats(data)),self)   
        # stats.setGeometry(120, 60, 600, 70)

        hp_label = QLabel("hp: ",self) 
        hp_label.setGeometry(50, 80, 600, 70)
        print(poke_stats['hp'])
        hp = QLabel(str(poke_stats['hp']),self) 
        hp.setGeometry(120, 80, 600, 70)

        attack_label = QLabel("attack: ",self) 
        attack_label.setGeometry(50, 100, 600, 70)

        attack = QLabel(str(poke_stats['attack']),self) 
        attack.setGeometry(120, 100, 600, 70)

        defense_label = QLabel("defense: ",self) 
        defense_label.setGeometry(50, 120, 600, 70)

        defense = QLabel(str(poke_stats['defense']),self) 
        defense.setGeometry(120, 120, 600, 70)

        special_attack_label = QLabel("special-attack: ",self) 
        special_attack_label.setGeometry(50, 140, 600, 70)

        special_attack = QLabel(str(poke_stats['special-attack']),self) 
        special_attack.setGeometry(120, 140, 600, 70)

        special_defense_label = QLabel("special-defense: ",self)
        special_defense_label.setGeometry(50, 160, 600, 70)

        special_defense = QLabel(str(poke_stats['special-defense']),self)
        special_defense.setGeometry(120, 160, 600, 70)

        speed_label = QLabel("speed: ",self) 
        speed_label.setGeometry(50, 180, 600, 70)

        speed = QLabel(str(poke_stats['speed']),self) 
        speed.setGeometry(120, 180, 600, 70)
         
         
         
         
        