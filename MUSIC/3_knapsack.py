def knapsack():
    val=[50,100,150,200]#value of goods
    wt=[8,16,32,40]##weight of goods
    W=64##capacity of bag
    n=len(val)##number of items

    dp=[[0]*(W+1)for _ in range(n+1)]##n+1 rows, W+1 columns

    for i in range(1,n+1):
        for w in range(1,W+1):

            if wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],
                             dp[i-1][w])
            
            else:
                dp[i][w]=dp[i-1][w]

    print(f"Maximum value that can be obtained:{dp[n][W]}")

knapsack()