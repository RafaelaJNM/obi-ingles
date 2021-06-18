#collect the information
N, D, Q = input().split()
N = int(N)#maximum the calculator supports
D = int(D)#dividend
Q = int(Q)#dividend


#creating a function for possible divisions
def aceita(a,b,c):
    R = b #dividendo
    P = c #divisor
    while a < R and a < P:
        R = b//10
        P = c//10
    return R, P


#showing the result
res = aceita(N,D,Q)
print(res)