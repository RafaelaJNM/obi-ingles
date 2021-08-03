#countdown -i

h = str(input())#word horizontally
v = str(input())#word vertically

ind_h, ind_v = -1, -1#starts with one minus for when there are no intersecting letters
ok = True

for i in range(len(h)-1,-1,-1):#minus one for him to go backwards
    for j in range(len(v)-1,-1,-1):
        if h[i] == v[j]:
            ind_h = i + 1# +1 because it starts counting from zero
            ind_v = j + 1
            ok = False
            break #stop the 1st loop of repetition
    if not ok:
        break #stop the 2nd loop repeat

print(ind_h, ind_v) #show the positions of the intersecting letters
