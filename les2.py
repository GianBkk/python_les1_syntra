# -------------------------FIRST FUNCTION-----------------------------------
x = [3, 4]

def func(x):
    x[0] = 2
func(x)
# List is mutable dus Verandert het Global
print(x)

# -------------------------FUNCTION-----------------------------------

def counter(y):

    while y <= 10:
        y += 1
        return print(y)

counter(1)


