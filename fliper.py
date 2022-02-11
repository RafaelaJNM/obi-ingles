#certo 2014

p, r = input().split()#seeing in which positions the doors are
r = int(r)#converting value to integer
p = int(p)#converting value to integer

if p == 0:#checking ports
    print('C')
elif p == 1:
    if r == 0:
        print('B')
    else:
        print('A')