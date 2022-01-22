#certo
n = int(input())# ball size

a,l,p = input().split()
a = int(a)# box height
l = int(l)# box width
p = int(p)# box length

if n <= a and n <= p and n <= l:##checking if the ball is less than or equal to the measurements of the box
    print('S')
else:
    print('N')