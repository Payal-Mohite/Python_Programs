no=int(input("Enter terms:"))
n2=1
n1=0
count=0
print("Fibonacci series")
while count<no:
    print(n1)
    nth=n1+n2
    #update values
    n1=n2
    n2=nth
    count+=1
