#taking the positions of three players(whole numbers)
L, R, D = input().split()
L = int(L)
R = int(R)
D = int(D)

#Evantuating the values for possible impediment
if R > 50 and L < R and R > D:
    print('S')
else:
    print('N')