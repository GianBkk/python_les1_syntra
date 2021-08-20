# Project 2 Advanced
# ---------------------------------------------------------------
# Create Player
# Live score System
# Number Guessing Game
# See Detail of Player
# Remove Player
# ---------------------------------------------------------------

# Imports

import random, datetime, time
player_list = []
player = False

class Player:

    def __init__(self, name, list):
        self.name = name
        self.score = 0
        self.amount = 0
        self.start = str(datetime.date.today())

    def config(self):
        print('------------------------------------------------------------------------------------------')
        print(self.name, '||', self.score, 'Punten ||', self.amount, 'Pogingen || created at:', self.start)
        print('------------------------------------------------------------------------------------------')

    def remove(self):
        del self

    def update(self, name):
        self.name = name






while True:
    if player == False:
        print('Welkom Bij Dit Speletje!')
        start = input('Click Enter om te beginnen ...')
        if start == '':
            setup = input('Als u Nieuw bent click (Enter) ander u Gebruikersnaam intoetsen ...')

            if setup == '':
                naam = input('Typ een Niew Gebuikersnaam in ...')
                if naam not in player_list:
                    speler = Player(naam, player_list)
                    player_list.append(speler)
                    print(player_list)
                    player = True
                else:
                    print('Gebruikersnaam existeet al!')
            elif setup.name in player_list:
                print('Speler Existert niet!')
            else:
                print('Speler Existert niet!')
    else:
        print(speler.name)
        player = False


