# Master Kung é o número 1.Master Lu, tem o número 9.

#we get the list of values
p = [int(i) for i in input().split()]

#we find the positions of the 2 players
for i in range(len(p)):
    if p[i] == 1:
        k = i+1#was getting your number and not position
    elif p[i] == 9:
        l = i+1#+1 because it starts at 0

#we put in order from smallest to largest
if k > l:
    k, l = l, k

#analyzing the position and seeing when they will face each other
if k <= 8 and l > 8:
    print('final')
elif k <= 4 and l > 4 or k <= 12 and l > 12:
    print('semifinal')
elif k % 2 == 1 and l == k + 1:
    print('oitavas')
else:
    print('quartas')