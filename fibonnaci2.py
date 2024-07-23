nth=int(input("Enter the nth fibonnaci number: "))
def fib(n):
    first=0
    second=1
    third=first + second

    if nth==3:
        print("1")
    elif nth==0:
        print("0")
    else:
        for i in range(1,nth-2):
            first=second
            second=third
            third=first+second
        print(third)
            
fib(nth)