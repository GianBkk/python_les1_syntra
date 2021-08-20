import random

# --------------------Project 1----------------------------------------------------


i = 1
s = 0
# Geen Idee Of Dit Nodig Is
user = {}
loop = ''
player = True
play = True
check = False

# Loop Voor Het Spel

while i == 1:
    if player == True:
        new = input('Wilt u een Niewe Player Toevoegen?(Y/N) ...')
        if user == {} or new.upper() == 'Y':
            player = True
            # Nieuwe Speler
            current = input('Enter New Username ...')
            score = 0
            user[current] = score

        else:
            # Bestaande Speler
            print('All users \n', user)
            player = False
            current = input('Input Your Username ...')
            loop = current
            score = user[current]
            play = True




    # Hier Beginnt Het Spel
    if current == loop:

        if play == True:
            print('Alleen', current, 'mag Spelen!\n')
            score = user[current]
            print('Dit is u huidige score:', score, 'Probeer het te verhogen!\n')
            print('Laat het spel Beginnen !')
            score += 1000
            goal = random.randint(1, 10)

            # Hier Komt De Eerste Input

            answer = int(input('Kies en Nummer tussen 1 - 10 ...'))
            if 1 < answer < 10:
                s += 50
                score -= s

                if answer > goal:
                    print('Overige Punten', score)
                    answer = int(input('Het Antwoord is Lager Probeer opnieuw ...'))

                elif answer < goal:
                    print('Overige Punten', score)
                    answer = int(input('Het Antwoord is Hoger Probeer opnieuw ...'))


            else:
                print('Uw Antwoord is niet binnen de lijnen!\n')
                score -= 500
            # De Gewonnen Score
            print('\nProficiat')

            print('U heeft', score, 'Punten!\n')

            # Het Veranderen Van De LeaderBoards

            user[current] = score
            game = input('Wilt u Nog een keer Spelen?(Y/N)')

            # Het Beeindige Van Het Spel

            if game.upper() == 'Y':
                print('\n', user)
                player = False
                play = True
            else:
                print('\n', user)
                play = False
                player = True








