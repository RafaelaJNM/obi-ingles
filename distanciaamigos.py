
#take the values
n = int(input())
p = [int(i) for i in input().split()]

#variables
dist0 = 0
k = -1

#calculates the greatest distance of two apartments
for i in range(n):
    d0i = p[0] + i + p[i]
    if d0i > dist0:
        dist0 = d0i
        k = i
#review if this value is the highest
maxdist = 0
for i in range(n):
    if i != k:
        maxdist = max(maxdist, p[k] + abs(k-i) + p[i])#funçao dentro da função

#show the value
print(maxdist)