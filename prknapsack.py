def solve():
    val=[50,100,150,200]
    wt=[8,16,32,40]
    W=64
    n=len(val)-1
    def kp(W,n):
        if W<=0 or n<0:
            return 0
        if wt[n]>W:
            return kp(W,n-1)
        else:
            return max(val[n]+kp(W-wt[n],n-1),kp(W,n-1))
    print(kp(W,n))
if __name__=="__main__":    
    solve()