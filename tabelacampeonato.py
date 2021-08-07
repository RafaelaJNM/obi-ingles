j,p,v,e,d = [int(i) for i in input().split()]
#games, points, wins, draws, losses
#when any value is equal to -1, it means it is unreadable

if j == -1:
    tj1,tj2 = 0,101101#value is 100 because this is the maximum value
#allowed in restrictions, and has 1 at the end, because in python
#always repeats in a for up to the penultimate number, if it were 100 it would repeat up to 99
else:
    tj1,tj2 = j,j+1
if p == -1:
    tp1,tp2 = 0,301#the score is 301 because the wins go if times 3
#so you need a bigger number
else:
    tp1,tp2 = p,p+1
if v == -1:
    tv1,tv2 = 0,101
else:
    tv1,tv2 = v,v+1#this value of plus one is because we already have the number,
# so we won't have to keep repeating it over and over to find the value
#not for
if e == -1:
    te1,te2 = 0,101
else:
    te1,te2 = e,e+1
if d == -1:
    td1,td2 = 0,101
else:
    td1,td2 = d,d+1

for tj in range(tj1,tj2):#If we have this value it will be repeated only once
    for tp in range(tp1,tp2):#if not it will repeat itself up to 101 looking for the value
        for tv in range(tv1,tv2):#
            for te in range(te1,te2):#
                for td in range(td1,td2):#
                    if tj == tv + te + td and tp == 3*tv + te:
                        #o if confirms that all values are "aligned"
                        print(tj,tp,tv,te,td)#