#taking the values of the three cards
a = int(input())
b = int(input())
c = int(input())
d = 0

#analyzing what is the different card
if a == b:
    d = c
elif a == c:
    d = b
elif b == c:
    d = a

#showing the result
print(d)