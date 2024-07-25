#bài 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
n =float (input('nhập vào số n1:'))
print(3*n+1)
#bài 2:Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
n =float((input('nhập vào số n2:')))
print(n**2/3)
#bài 3:Nhập vào nhiệt độ c, in ra nhiệt độ F
c =float((input('nhập vào nhiệt độ c3:')))
f = c*1,8+32
print(f)
#bài 4:Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
a =int(input('nhập vào số nguyên a4:'))
print(a % 2==0)
#bài 5:Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
a =int(input('nhập vào số nguyên a5:'))
print(a % 3 ==0 and 50 <= a<= 100 )
#bài 6:Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
a = int(input('nhập vào số nguyên a6 :'))
print(a % 5 ==0 and not (20 <= a <= 70))
#bài 7:Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False    
a =int(input('nhập vào số nguyên a7:'))
b =int(input('nhập vào số nguyên b7:'))
print(a % 2 == 0 or b % 2 ==0)
#bài 8:Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
a =float(input('nhập vào số thực a8:'))
#lệnh làm tròn
b = round(a)
print(a==b)
#bài 9:Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
a = int(input('nhập vào số nguyên a9:'))
cana = a**0.5
print(cana == round(a))
#bài 10:Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
salary = int(input('nhập vào lương tháng này nhận được:'))
print("lương giữ lại là:",salary*0.1)
#bài 11:Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
a = int(input('nhập vào số a11: '))
b = int(input('nhập vào số b11: '))
c = int(input('nhập vào số c11: '))
print(a+b+c)
#bài 12:Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c,
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a = int(input('nhập vào số a12: '))
b = int(input('nhập vào số b12: '))
c = int(input('nhập vào số c12: '))
d =(a+b)^c
