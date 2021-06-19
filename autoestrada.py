c = int(input())# 1 = 10metros
cara = str(input()).upper()#the .upper function is to capitalize all letters
nome = list(cara)#the list() function serves to separate each letter or a word

#creating a fuction to analyze each letter and see its corresponding value
def separa(a,b):
    tot = 0
    for i in range(a):
        if b[i] == 'P' or b[i] == 'C':
            tot += 2
        elif b[i] == 'A':
            tot += 1
        elif b[i] == 'D':
            tot += 0
    return tot

#printing the value
print(separa(c, nome))
