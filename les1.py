
txt = 'mango\'s'
num = 1


while(num != 11):
    print('There are ...\n', num , txt)
    num += 1
num = 0
while(num != 7):
    print(txt[num])
    num += 1

# --------------------------------Concept Tupels-----------------------------------

t = (0, 2, 4)

# This is a Comment about this piece of Code
print(2 in t) # Python is beautiful
print(type(2 in t))

# --------------------------------Concept Lists/Arrays-----------------------------------

a = [0, 3, 2, 3, 8]

a.append(2)
print(a)
a.remove(3)
print(a)
a.pop(0)
print(a)

d = [[1, 2, 3], [4, 5, 6]]

print(d[1][2])

# --------------------------------Concept Set-----------------------------------

b = {2, 3, 4, 5}

print(b)
# Dit werkt niet omdat set geen duplicate is
b.add(2)
print('niks verandert',b)
# Dit werkt omdat het geen duplicate is
b.add(6)
print(b)

# --------------------------------Concept Dictionaries-----------------------------------

c = {'b': 1, 'c' : 5} # c is en dict

print('Dict Naam b = ', c['b'])
c['d'] = 3
print(c)

del c['b']
print(c)

# --------------------------------Concept LOOPS-----------------------------------

for i in range(10):
    print(i)

# --------------------------------Concept LOOPS/WHILE-----------------------------------
x = 4

while not 0 < x < 10:
    x = int(input('Enter Number'))


# --------------------------------Concept LOOPS/WHILE---------------------------------





