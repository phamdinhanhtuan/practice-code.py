#bai 30:Nhập vào số nguyên dương a, đếm số ước của a
a = int(input("Nhap so a : "))
dem = 0
for i in range(1,a+1):
    if a % i == 0:
        dem += 1
print(dem)
#bai31:Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
a = int(input('Nhap vao a: '))
b = int(input("Nhap vao b : "))
for i in range(1,a+1):
    if i > b:
        break
if a % i ==0 and b % i ==0:
    print(i)
#bai 32:Nhập vào số nguyên dương a và b, in ra ước chung  lớn nhất  của a và b
a = int(input('Nhap vao so a '))
b = int(input('Nhap vao so b '))
UCLN =1
for i in range(1,a+1):
    if i > b:
        break
if a % i ==0 and b % i ==0:
    UCLN = i
print(UCLN)
#33:Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
a = int(input("Nhap so nguyen a : "))
if a >1:
 dem = 0 
 for i in range(1,a+1):
    if a % i ==0 :
        dem += 1
    if dem == 2:
        print('a là số nguyên tố')
else :
    print("a không phải là số nguyên tố")
    