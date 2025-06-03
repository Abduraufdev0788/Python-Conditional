import os

file = input("fayl nomini kiriting : ")

if os.path.exists(file) :
    print(f"fayl {file} mavjud.")
else:
    print(f"Fayl {file} topilmadi.")    
