# 2014 certo
#if the seesaw is balanced, print('0'). if she id out of balance so that the left child is
#at the bottom, print(-1), otherwise , print(1)

p1,c1,p2,c2 = input().split()#values
p1 = int(p1)#weight pf the first child
p2 = int(p2)#weight of the second child
c1 = int(c1)#size side 1 gives seesaw
c2 = int(c2)#size of seesaw side

if p1*c1 == p2*c2:#sell if they are balanced
    print('0')
elif p1*c1 > p2*c2:#checking the left side is heavier
    print('-1')
else:#or directly
    print('1')