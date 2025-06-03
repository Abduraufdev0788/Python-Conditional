ball = int(input("ballni kiriting: "))
if 0 <= ball <= 100 :
    if 90 <= ball <= 100 :
        print("a'lo")
    elif 80 <= ball <=89 :
        print("yaxshi")
    elif 70 <= ball <=79 :
        print("qoniqarli")
    elif 60 <= ball <=69 :
        print("qoniqarsiz")
    elif 0<= ball <=59 :
        print("rad") 
else :
    print("Ball 0-100 oralig'ida bolishi kerak")                       