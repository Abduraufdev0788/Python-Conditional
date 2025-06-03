password = input("parolingizni kiriting: ")


if len(password) >= 8 and password.isalnum() and not password.isdigit() and not password.isalpha():
    print("parol qabul qilindi")
    
else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")            
            