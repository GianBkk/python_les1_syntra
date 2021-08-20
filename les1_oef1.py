import random

print(2+4)

print(4**2)

print('Ik ben', 18)

if(3 == 4):
    print('Niet gelijk!')
else:
    print('Wel gelijk!')

g1 = 3
g2 = 5

if(g2 > g1):
    print(g2)


g3 = input('Enter Number ...')
g4 = input('Enter Number ...')

if(g3 == g4):
    print('Gelijk!')
elif(g3>g4):
    print('Groter:',g3 , 'Kleiner:', g4)
elif(g3<g4):
    print('Groter:',g4 , 'Kleiner:', g3)
else:
    print('Dit is en Error')


g5 = int(input('Enter Number between 0 - 10 ...'))

if(g5 >= 10):
    while(g5 >= 10):
        g5 = int(input('Kies en getaal kleiner of gelijk aan Tien ...'))
        if(g5 <= 10):
            break
        else:
            print('Doe op nieuw')
else:
    print('Not a Number')

print('Proficiat')





