#bai 30:Nhập vào số nguyên dương a, đếm số ước của a
a = int(input("Nhap so a : "))
dem = 0
for i in range(1,a+1):
    if a % i ==0:
        dem +=1
print(dem)
        