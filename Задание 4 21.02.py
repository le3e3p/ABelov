a=int(input())
if 9999<a>=99999:
    b=(a%100)//10
    c=(a%100)%10
    print(b,c)
else:
    a=int(input("Введите пятизначное число"))
    b=(a%100)//10
    c=(a%100)%10
    print(b,c)
