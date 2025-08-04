#الواجهة 
print("**********************************************************************************************************************")
print("******####******####********#*********####******##*****##******#********####**********#**********####******##*###*****")
print("****##********##****##******#*******##**********##*****##******#******##****##******#####******##****##******#********")
print("****##********##****##******#*******##**********##*****##******#******##****##********#********##****##******#********")
print("******####******####*##*****##********####********#####********##*******####*##*******###********####********#********")
print("**********************************************************************************************************************\n")

print("The oprations that you can use : | + | - | * | / | remainder of division | ^ | absolute value | round | square root |")

#المتغيرات
num1= int(input ("Enter the first numper: "))
op =  input ("Enter the opration: ")
num2= int(input ("Enter the second numper: "))
#الجمع
if op == "+":
    print("The value is :"+str(num1+num2))
#الطرح
elif op == "-":
    print("The value is :"+str(num1-num2))
#الضرب 
elif op == "*":
    print("The value is "+str(pow(num1,num2)))
#القسمة
elif op =="/":
    print("The value is "+str(num1/num2))
#المتبقي
elif op == "%":
    print("The value is "+str(num1%num2))
#الاس 
elif op == "^":
    print("The value is "+str(num1^num2))
#القيمة المطلقة
elif op == "absolute value":
    print("The value is "+str(num1,num2))
#التقريب
elif op == "round":
    print("The value is "+str(num1,num2))
#الجذر التربيعي
elif op == "square root":
    print("The value is "+str(num1,num2))
#المساعدات
else:
    print("Error...")
