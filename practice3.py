#Bài 23:In 10 lần chữ hello ra màn hình
for i in range(10):
    print('hello')
#Bài 24:In các số lẻ dương bé hơn 100
for i in range(1,100):
    if i % 2==0:
        print(i)
#Bài 25:In các số chẵn chia hết cho 3 bé hơn 100
for i in range(1,100):
    if(i % 3 == 0 and i % 2 ==0):
        print(i)
#Bài 26:Nhập vào số nguyên dương a, in ra bảng cửu chương của a
a = int(input('Nhập số nguyên dương a:'))
for i in range(1,10):
    print(a,'X',i,'=',a*i)
#Bài27:Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
h = int(input('Nhập vào chiều cao h:'))
khoangtrangngoai = h-1
khoangtrangtrong = 1
for i in range(h):
    if i == 0:
        print(" "*khoangtrangngoai + "*" )
    elif i < h -  1:
        print(" "* khoangtrangngoai +"*"+ " "* khoangtrangtrong +"*")
        khoangtrangtrong += 2
    else:
        print("*"* (h*2-1))
    khoangtrangngoai -= 1


     
        