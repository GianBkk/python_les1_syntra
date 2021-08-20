import random, datetime

# --------------------Project 2----------------------------------------------------
player = False
i = 0
user = []
score = []
pogingen_List = []
date_list = []

# Maak een Speler aan

def Player():
    temp = input('Maak een Nieuwe Speler aan ...')
    user.insert(0, temp)
    i = CheckPlayer(temp)
    score.insert(0, 0)
    pogingen_List.insert(0, 0)
    date_list.insert(0, datetime.date.today())
    player = True
    return player, i


# Checken van Spelers

def CheckPlayer(name):
    i = user.index(name)
    return i

# Het Spel

def Spel(speler):
    print('--------------------------------------------------')
    print('Het Spel Beginnt Nu!\n')
    goal = random.randint(0, 100000)
    num = input('Kies een Nummer tussen 0 en 100.000')
    num = int(num)
    if 0 < num < 100000:
        if num != goal:
            print('Helaas het Nummer moest:', goal, 'zijn!')
            livescore = Score(num, goal)
            if livescore < score[speler]:
                livescore = score[speler]
                print('Helaas Niet verbeterd')
            print('U heeft hiermee:', livescore, 'Punten')
        else:
            print('Proficitat uw heeft een Jackpot!!!!')
            livescore = 100000

    else:
        livescore = 0
    score[speler] = livescore
# De Score

def Score(num, goal):
    if num < goal:
        return 100000 - (goal - num)
    elif num > goal:
        return 100000 - ((goal - num) * -1)


# Het ScoreBoard

def ScoreBoard():
    print('--------------------------------------------------')
    for i in range(len(user)):
        print('||', user[i], '||', score[i], 'Punten ||')
        print('--------------------------------------------------')

# Status van de Speler

def Stats(speler):
    pogingen = pogingen_List[speler]
    register = date_list[speler]
    currentscore = score[speler]
    speler = user[speler]
    print('---------------------------------------------------------------------')
    print('||', speler, '||', currentscore, 'Punten || Pogingen:', pogingen, '|| Created at:', register)
    print('---------------------------------------------------------------------')

# Poging Counter

def Pcount(speler):
    pogingen_List[speler] = pogingen_List[speler] + 1


# Remove Player

def Remove(speler):
    rm = input('Weet u dit Zeker?(Enter = ja, q = Nee)')
    if rm == '':
        user.pop(speler)
        score.pop(speler)
        pogingen_List.pop(speler)



# Main Loop

while True:
    if player == False:
        print('--------------------------------------------------')
        print('Dit is een Spel van Gian!\n')
        if not user:
            check = Player()
            player = check[0]
            i = check[1]
        else:
            name = input('Als u Nieuw bent typ (Enter) anders Typ uw Gebruikersnaam ...')
            if name in user:
                i = CheckPlayer(name)
                player = True
            elif name == '':
                check = Player()
                player = check[0]
                i = check[1]
            else:
                print('Not a valid user (try again)')
    elif player == True:
        Spel(i)
        Pcount(i)
        ScoreBoard()
        temp = input('Wilt u nog een Keer Spelen?(Enter = Ja, q = Nee, m = Meer info)')
        if temp == 'm':
            Stats(i)
            rm = input('Wat wilt u doen?(Enter = Spelen, q = Quit, r = Remove)')
            if rm == 'r':
                Remove(i)
                ScoreBoard()
            elif rm == '':
                temp = ''
        if temp != '':
            print('\nBedankt voor het Spelen!\n')
            player = False


