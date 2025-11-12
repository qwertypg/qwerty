def fibo_iter(n:int):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        prev,curr=0,1
        for _ in range(3,n+1):
            prev,curr=curr,prev+curr
        return curr
        

def fibo_recur(n:int):

    if n==1:
        return 0
    elif n==2:
        return 
    
    else:
       return fibo_recur(n-1)+fibo_recur(n-2)

def main():
    print("--------Fibonacci results--------")
    print("1)Fibonacci Iterative")
    print("2)Fibonacci Recursive")

    choice = int(input("Enter choice (1/2): "))
    n = int(input("Enter value of n: "))

    
    if choice==1:
        print(f"Fibonacci Iterative={fibo_iter(n)}")

    if choice==2:
        print(f"Fibonacci Recursive={fibo_recur(n)}")


if __name__=="__main__":
    main()




