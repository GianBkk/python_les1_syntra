import random


# --------------------Project 1----------------------------------------------------


i = 1

#Geen Idee Of Dit Nodig Is
user = {}

#Loop Voor Het Spel

while i == 1:

    exist = input('Are You New? (Y/N)')

    if exist.upper() == 'Y':
        # Nieuwe Speler
        current = input('Enter New Username ...')
        score = 0
        user[current] = score
        x = input('Wilt u nog een Speler toevoegen(Y/N)')
        if x == 'N':
            print('All users \n', user)
            current = input('Input Your Username To Play ...')
            loop = current
            score = user[current]
        else:
            loop = ''


    else:
        #Bestaande Speler
        print('All users \n', user)
        current = input('Input Your Username ...')
        loop = current
        score = user[current]


# Hier Beginnt Het Spel
    while current == loop:


        print('Alleen', current, 'mag Spelen!')
        score += 1000
        print('Dit is u huidige score:', score, 'Probeer het te verhogen!')
        print('Laat het spel Beginnen !')
        goal = random.randint(1, 10)

    # Hier Komt De Eerste Input

        answer = int(input('Kies en Nummer tussen 1 - 10 ...'))

        while answer != goal:
            #Dit Gebeurt Als De Player Een Min Getal Input

            while answer < 0:
                score -= 500
                print('Overige Punten', score)
                answer = int(input('Bruh... u bent Negative :('))

            if answer > goal:
                while answer > goal:
                    score -= 100
                    print('Overige Punten', score)
                    answer = int(input('Het Antwoord is Lager Probeer opnieuw ...'))
            elif answer < goal:
                while answer < goal:
                    score -= 100
                    print('Overige Punten', score)
                    answer = int(input('Het Antwoord is Hoger Probeer opnieuw ...'))
            else:
                #Geen Nummer

                print('There was an Error')

        #De Gewonnen Score

        print('U heeft', score, 'Punten!')

        #Het Veranderen Van De LeaderBoards

        user[current] = score
        game = input('Wilt u Nog een keer Spelen?(Y/N)')

        #Het Beeindige Van Het Spel

        if game.upper() == 'Y':
            print(user)
        else:
            print(user)
            loop = ''







