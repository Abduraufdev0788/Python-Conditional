vazn = float(input("vazninigzni kiriting "))
height = float(input("bo`yingizni olchamini kiriting: "))

if 0.5 <= height <= 3 and 1 <= vazn <=500 :
    BMI = vazn / (height*height)
    
    if BMI < 18.5 :
        print("kam vazn")
    elif 18.5 <= BMI < 25 :
        print("normal vazn")
    elif 25 <= BMI < 30 :
        print("ortiqcha vazn")
    else :
        print("semizlik") 
elif height <0 or vazn < 0 :
    print("manfiy qiymat kiritildi")
else :
    print("format notogri kiritilgan")