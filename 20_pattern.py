'''
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print("*",end="")
    print("")


'''
A B C D 
A B C D 
A B C D 
A B C D 

'''

for i in range(65,69):
    for j in range(65,69):
        print(chr(j),end="")
    print("")



'''
*
**
***
****
'''
for i in range(5):
    for j in range(0,i+1):
        
        print("*",end="")
    print("")
    
'''
****
***
**
*

for i in range(5):
    for j in range(i,5):
         print("*",end="")
    print("")'''


n=0
rows=3
for i in range(1,rows+1):
    for j in range (1,(rows-i)+1):
        print(end=" ")
        while n!=(2*i-1):
            print("*",end=" ")
            n=n+1
            n=0
            print()
            k=1
            n=1
            for i in range(1,rows):
                for j in range(1,k+1):
                    print(end=" ")
                    k=k+1
                    while n<=(2*(rows-i)-1):
                        print("*",end=" ")
                        n=n+1
                        n=1
                        print()
            





