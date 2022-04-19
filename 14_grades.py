# program that takes the marks of 5 subjects and displays the grade
sm=0
for i in range(5):
    marks=int(input("Enter marks of sub"))
    sm=sm+marks
print("Sum of marks is:",sm)
per=sm*100/500
print("Percentage:",per)

if(per>35 and per<=50):
    print("Pass")
elif(per>50 and per<=70):
    print("Distinction")
elif(per>70 and per<=80):
    print("Grade B")
elif(per>80 and per<=100):
    print("Grade A")
else:
    print("Fail")
