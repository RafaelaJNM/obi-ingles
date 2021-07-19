#number of rows and columns on the board
n = int(input())
tab = []

#assembling the board
for i in range(n):
    nes = [int(i) for i in input().split()]
    tab.append(nes)

#row and column position
for i in range(1,n):
    for j in range(1,n):
        #claculating whether there is more black or white
        if tab[i][j-1] + tab[i-1][j-1] + tab[i-1][j] >1:
            tab[i][j] = 0
        else:
            tab[i][j] = 1

#printing the last position
print(tab[n-1][n-1])