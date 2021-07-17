# Take the values
C = int(input())
A = int(input())

# calculate student trips
quociente = A // (C - 1)

# how many students are letf
resto = A % (C - 1)

# if there is a student left, you have +1 trip
if resto > 0:
    quociente += 1

# Shows the value
print(quociente)
