from time import sleep
import sys
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength
import requests


class Pokemon():
    def __init__(self, name):
        self.name = name
        self.types = []
        self.abilities = []
        self.weight = None
        self.image = None
        self.moves = []
        self.poke_api_call()
        
    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f"Please check the spelling of your pokemon's name and try again!: {r.status_code}")
            return
        self.moves = pokemon['moves']
        self.name = pokemon['name']
        self.types = [type_['type']['name'] for type_ in pokemon['types']]
        self.abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        self.weight = pokemon['weight']
        #new image details. adding image to attribute
        self.image = pokemon['sprites']['front_shiny']
        print(f"{self.name}'s data has been updated!")

        return self.name
    
    #display our image with a method
    def display_image(self):
        display(Image(url = self.image))

    #repr gives us string representation of our object
    def __repr__(self):
        self.display_image()
        return f"You caught a {self.name}!"


class Move_Tutor(Pokemon):
    def __init__(self,name):
        Pokemon.__init__(self,name)
        self.move_list = []
        self.taught_moves = []

    def progress_bar(self):
        widgets = [f'Teaching {self.name} {self.move} ', AnimatedMarker(markers='◢◣◤◥')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            sleep(0.3)


    def teach_move(self,move):
        self.move = move
        self.move_list = self.moves
        for moves in self.move_list:
            if moves['move']['name'] == self.move:
                self.progress_bar()
                print(f"{self.name} now knows {self.move}!")
                self.taught_moves.append(self.move)
                break        
        else:
            print(f"{self.move} is not available")

        print(self.taught_moves)
        


squirtle = Move_Tutor('squirtle')
squirtle.teach_move('bite')
squirtle.teach_move('mist')
squirtle.teach_move('water-gun')
squirtle.teach_move('ice-beam')
