from math import *
#الواجهة 
print("**********************************************************************************************************************")
print("******####******####********#*********####******##*****##******#********####**********#**********####******##*###*****")
print("****##********##****##******#*******##**********##*****##******#******##****##******#####******##****##******#********")
print("****##********##****##******#*******##**********##*****##******#******##****##********#********##****##******#********")
print("******####******####*##*****##********####********#####********##*******####*##*******###********####********#********")
print("**********************************************************************************************************************\n")
#المساعدات
print("The oprations that you can use : | + | - | * | / | remainder of division | ^ | absolute value | round | square root |")

#المتغيرات

op = input("enter the operation: ")

if op in ["+" , "-" , "*" , "/" , "remainder of division" , "^"]:
    num1= float(input ("enter the first numper: "))
    num2= float(input ("enter the second numper: "))
   #الجمع
    if op == "+":
        print("the value " +str(num1+num2))
#الطرح
    elif op == "-":
        print("The value is "+str(num1-num2)) 
#الضرب 
    elif op == "*":
        print("The value is "+str(num1*num2))  
#القسمة
    elif op =="/":
        print("The value is "+str(num1/num2))
#المتبقي
    elif op == "%":
        print("The value is "+str(num1%num2))
#الاس 
    elif op == "^":
        print("The value is "+str(pow(num1,num2)))
    else:
        print("erro")



elif op in ["absolute value" , "round" , "square root"]:
    num1= float(input ("enter the numper: "))
    #القيمة المطلقة
    if op == "absolute value":
        print("The value is "+str(abs(num1)))
#التقريب
    elif op == "round":
        print("The value is "+str(round(num1)))
#الجذر التربيعي
    elif op == "square root":
        if num1 >= 0:
            print("The value is "+str(sqrt(num1)))
        else:
            print("error")

#error
else:
    print("Error...")
