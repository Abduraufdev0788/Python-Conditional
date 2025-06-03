num1 = float(input("1-sonni kiriting: "))
num2 = float(input("2-sonni kiriting: "))
amal = input("amalni kiriting: ")

#b = "Natija: {num1} {amal} {num2} =".format(num1 == num1, num2==num2, amal==amal)
if amal == "*" or amal == "+" or amal == "-" or amal == "/" :
    if amal == "/" and num2 == 0 :
        print("nolga teng bolishi mumkin emas")
    elif amal == "/" and not num2 == 0 :
        a = num1 / num2
        print(f"Natija: {num1} {amal} {num2} = {a}")
    elif amal =="*" :
        a = num1*num2
        print(f"NAtija : {num1} {amal} {num2} = {a}")
    elif amal =="+" :
        a = num1 + num2
        print(f"NAtija : {num1} {amal} {num2} = {a}")
    elif amal== "-" :
        a = num1-num2
        print(f"NAtija : {num1} {amal} {num2} = {a}")        
        
        