import math
x=input("Nhap gia tri x: ")
x=float(x)
f_x=math.log (x,4) + math.log(2,x)
if x >= 2:
  print(f"Gia tri can tim f(x)={f_x:.2f}")
else:
    print("Loi phep tinh")
