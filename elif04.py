distance = float(input("masofani kiriting: "))

if distance >= 0 :
    if 0 <= distance <=1 :
        print("Piyoda yuring")
    elif 1 < distance <=5 :
        print("Velosiped yoki elektro skuter")
    elif 5 < distance <=50 :
        print("Avtobus yoki mashina")
    else:
        print("poyezd yoki samalyot")           
else :
    print("manfiy son kiritish mumkin emas")