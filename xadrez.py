#take the values
L = int(input())
C = int(input())

#finds out if the rest of the split is even or odd

li = L % 2
cp = C % 2

#calculates the result
res = 0
if li == 1 and cp == 0 or cp == 1 and li == 0:#that part of the code can be removed
    res = 0#because the res receiveis the value it already is
elif li == 0 and cp == 0 or li == 1 and cp == 1:
    res = 1

#shows the value
print(res)
