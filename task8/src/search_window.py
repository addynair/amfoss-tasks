
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
import requests
from PySide6.QtGui import QPixmap, QMovie
from poke_window import PokeWindow

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
       
        # self.textbox.setStyleSheet("""position: absolute""" )

       
        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 850, 500) 

        background_image = QPixmap("../assets/landing.png")  
        background_label.setPixmap(background_image)

      
        
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

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)

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
        poke_name = self.textbox.text()
        response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(poke_name))
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
        if self.w is None:
            self.w = PokeWindow()
        self.w.show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
