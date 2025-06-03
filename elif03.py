time = int(input("soatni kriting: "))

if 0 <= time <= 23 :
    if 5 <= time <= 11 :
        print("ertalab")
    elif 12 <= time <= 17 :
        print("kunduzi")
    elif 18 <= time <= 21 :
        print("kechqurun")
    else:
        print("tun")
else:
    print("Soat 0-23 oraligida bolishi kerak!")            