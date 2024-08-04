#bài 14:Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
a = int(input('Nhập vào số nguyên dương a14:'))
if (a%2 == 0):
    print('a là số chẵn')
else:
    print('a là số lẽ')
#bài 15:Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
a = float(input('Nhập số thực dương a15: '))
b = float(input('Nhập số thực dương b15: '))
c = float(input('Nhập số thực dương c15: '))
if (a+b> c and a+c > b and c+b> a):
    print('a,b,c có thể tạo thành 1 tam giác')
else:
    print('a,b,c không thể tạo thành 1 tam giác')
#bài 16:Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
a = float(input('Nhập số thực dương a16:'))
b = float(input('Nhập số thực dương b16:'))
c = float(input('Nhập số thực dương c16 '))
if (a+b> c and a+c> b and b+c> a):
    if (a == b == c):
        print(' a,b,c,có thể tạo thành 1 tam giác')
    elif (a == b or b == c or c == b):
# ta sử dụng định lí pytago  
        if (a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 +c **2 or c ** 2 == b ** 2 +a ** 2):
          print('Đây là tam giác vuông')
        else:
            print('Đây không phải tam giác vuông')
    elif (a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 +c **2 or c ** 2 == b ** 2 +a ** 2):
        print('a,b,c là tam giác vuông')
    else :
        print('a,b,c là tam giác thường')
else :
    print('a,b,c không thể tạo thành 1 tam giác')
#bài 17: Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
a = int(input('nhập vào số a17:'))
b = int(input('nhập vào số b17:'))
c = int(input('nhập vào số c17:'))
sorted_list = sorted([a,b,c])
a,b,c = sorted_list
print('Thứ tự tăng dần',a,b,c)
#bài 18: Giải và biện luận phương trình ax + b = 0
a = float(input('nhập số a18 :'))
b = float(input('nhập số b18:'))
print("phương trình ta có "+ str(a) + " X + "+ str(b)+ "=0")
if a ==0 :
     if b == 0:
         print('Đây là phương trình vô sô nghiệm')
     else:
         print('Đây là phương trình vô nghiệm')
else:
    print('Đây là có nghiệm ',-b/a)
#bài 19 :Giải và biện luận phương trình ax^2 + bx + c = 0
a = float(input('nhập số a19 :'))
b = float(input('nhập số b19 :'))
c = float(input('nhập số c19 :'))
print("phương trình" + str(a) + "x^2" + str(b) +"x" + str(c) + " =0")
if a == 0:
    if b == 0:
        if c == 0:
            print('Đây là phương trình vô số nghiệm')
        else:
            print('Đây là phương trình vô nghiệm')
    else:
        print('Đây là phương trình có nghiệm',-b/a)
else:
    delta = b ** 2 - 4 * a * c
    if delta >0:
        căn_delta = delta  ** 0.5
        x1 =(-b + căn_delta)/(2*a)
        x2 =(-b - căn_delta)/(2*a)
        print("phương trình có hai nghiệm phân biệt là: ",x1,x2)
    elif delta == 0:
        print("phương trình này có nghiệm kép",-b/(2*a))
    else :
        print("Đây là phương trình vô nghiệm ")
#bài 20:Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
thang = int(input('Nhập vào tháng: '))
nam = int(input('Nhập vào năm:'))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12 :
    print('tháng có 31 ngày ')
elif thang == 4 or thang == 6 or thang == 9 or thang == 11 :
    print(' tháng có 30 ngày ')
else:
#năm chia hết cho 400  và 4 nhưng ko hết cho 100(có nghĩa là chia hết cho 100 nhưng phần dư nó khác 0 ) 
# .vì 4 năm mới có 1 năm nhuần 
    if (nam % 400 == 0) or (nam % 4 == 0 and  nam % 100 != 0 ):
        print('Tháng có 29 ngày')
    else :
        print('Tháng có 28 ngày')
#bài 21:Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)
ngay = int(input('Nhập vào ngày:'))
thang =int(input('Nhập vào tháng:'))
if thang <= 8:
    sothang30ngay =(thang-1)//2
    sothang31ngay =(thang//2)
else:
    sothang30ngay = thang // 2 - 1
    sothang31ngay = (thang +1 )//2
songay = ngay + sothang30ngay*30 + sothang31ngay*31
if thang > 2 :
    songay -2
print(songay)    
#bài 22:Nhập điểm toán, văn, anh.
# Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
# Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
#Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
#Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
#Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
#Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
Toán = float(input('Nhập điểm môn toán: '))
Văn = float(input('Nhập điểm môn văn: '))
Anh = float(input('Nhập điểm môn anh:'))
if (0 <= Toán <= 10 and 0 <= Văn <= 10 and 0 <= Anh <=10):
    ĐTB = (Toán + Văn + Anh)/3
    if ĐTB >= 8 and (Toán >= 8 or Văn >= 8 ) and (Toán >= 6.5 or Văn >= 6.5 or Anh >= 6.5 ):
        print('Học sinh giỏi')
    if ĐTB >= 6.5 and (Toán >= 6.5 or Văn >= 6.5) and (Toán >= 5 or Văn >= 5 or Anh >= 5) :
        print('Học sinh khá')
    if ĐTB >= 5 and (Toán >= 5 or Văn >= 5) and (Toán >= 3.5 or Văn >= 3.5 or Anh >= 3.5) :
        print('Học sinh khá')
    if ĐTB >= 3.5 and (Toán >= 3.5 or Văn >= 3.5 ) and (Toán >= 2 or Văn >= 2 or Anh >= 2):
        print('Học Sinh trung bình ')
else:
    print('Bạn đã nhập sai quy tắc')

 
    

