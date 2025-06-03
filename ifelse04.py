total = 5000
sarf = int(input("sarflamoqchi summani kriting: "))

if sarf > 0:
    if total > sarf :
        a = total - sarf
        print(f"Pul yechildi. Qolgan balans: {a} so'm")
    else :
        print("Mablag' yetarli emas. Sizning balansingiz: 5000 so'm")
else :
    print("manfiy summa kiritib bolmaydi")    