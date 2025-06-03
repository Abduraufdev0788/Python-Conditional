gmail = input("emailingizni kiriting: ")

if "@" in gmail and ( ".com" == gmail[-4:] or ".uz" == gmail[-3:] or ".net" == gmail[-4:] or ".org" == gmail[-4]):
    print("emailingiz qabul qilindi")
else :
    print("emailingiz notogri formatda")
    
    
