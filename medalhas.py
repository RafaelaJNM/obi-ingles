
#create the folder to receive player time
tempos = []

for x in range(3):
    #take the times and add it to the list
    tempos.append((int(input()), x + 1))
    # the x+1 is for instead of the positions being 0.1 and 2 to get 1.2 and 3

#put in ascending order
tempos.sort()

#shows position of values
for tempo, indice in tempos:
    print(indice)
