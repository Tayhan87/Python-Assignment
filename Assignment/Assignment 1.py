bangla=int(input("Enter the marks of bangla: "))
english=int(input("Enter the marks of English: "))
math=int(input("Enter the marks Math of : "))
science=int(input("Enter the marks of Science: "))

avg = ((bangla+english+math+science)/4)

if avg<=40:
    result="F"
elif avg>40 and avg<=60:
    result="D"
elif avg>60 and avg<=70:
    result="C"
elif avg>70 and avg<=80:
    result="B"
elif avg>80 and avg<=90:
    result="A"

elif avg>90 and avg<=100:
    result= "A+"

print("The result is " , result)
