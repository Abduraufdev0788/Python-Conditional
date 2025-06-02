age = int(input("yoshingizni kiriting: "))

if 0 < age < 7 :
    price = 100 * 0.5
    print(f"yakuniy narx : {price} so`m (50 % chegirma qollanildi)")
if 7 <= age <= 17 :
    price = 100 * 0.8
    print(f"yakuniy narx : {price} so`m (20 % chegirma qollanildi)")
if 60 <= age :
    price = 100 * 0.7
    print(f"yakuniy narx : {price} so`m (30 % chegirma qollanildi)")    