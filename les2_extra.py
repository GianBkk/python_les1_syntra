

# Chapter 3 ---------------------------------------------------------------
# Nomalize List of Integers

myList = [5, 1, 2, 45, 8, 9, 3, 12, 23, 3, 5, 33, 21, 27, 8, 1, 34, 5, 23, 32]

max_value = max(myList)
min_value = min(myList)
for i in range(0, len(myList)):
    myList[i] = (myList[i] - min_value) / (max_value - min_value)

print(myList)

# --------------------------------CONVERT TO FLOAT------------------------------------------


myList = [5.0, 1, '2', 45, 8.0, 9, 3, 12, 23, 3, '5', 33, 21, 27, 8, 1, '34', 5, 23, 32.0]


myList = [float(i) for i in myList]

print(myList)

# ---------------------------------NAME/COUNTRY COMBINER-----------------------------------------

fName = ['Jean', 'Jef', 'Tom', 'Lucy', 'Joey', 'John']
lName = ['Jacques', 'Gorissen', 'Wever', 'Jones', 'Smith', 'Doe']
country = ['France', 'Belgium', 'England', 'England', 'USA', 'USA']


for idx, word in enumerate(fName):
    print(fName[idx], lName[idx], '-', country[idx])

# ----------------------------------TAX CALCULATOR----------------------------------------

income = float(input('Income ...'))

if income > 41360.01:
    tax = income * 50 / 100
elif 23900.01 < income < 41360:
    tax = income * 45 / 100
elif 13540.01 < income < 23.900:
    tax = income * 40 / 100
else:
    tax = income * 25 / 100


print('Total Income is: €', "{:.2f}".format(income), '\n Total Tax Rate is: €', "{:.2f}".format(tax))










