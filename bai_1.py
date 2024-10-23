pi = 3.14
r = float(input("Nhập bán kính (r): "))
h = float(input("Nhập chiều cao (h): "))
if r > 0 and h > 0:
    dtxq = 2 * pi * r * h
    dttp = 2 * pi * r * (h + r)
    the_tich = pi * r**2 * h
    
    print("Diện tích xung quanh:", dtxq)
    print("Diện tích toàn phần:", dttp)
    print("Thể tích:", the_tich)
else:
    print("Bán kính và chiều cao phải lớn hơn 0.")
 
