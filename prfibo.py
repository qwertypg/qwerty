def fiboi(n:int):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        dp=[0]*n
        dp[0]=0
        dp[1]=1
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]  
def fibor(n:int):
    c={1:0,2:1}
    return help(n,c)

def help(n:int,c):
    if n in c:
        return c[n]
    else:
        c[n]=help(n-1,c)+help(n-2,c)
        return c[n]

n=int(input())
print(fiboi(n)) 
print(fibor(n))