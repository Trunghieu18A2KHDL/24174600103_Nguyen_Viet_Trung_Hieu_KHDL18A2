x=float(input("Nhao gia tri cua x"))
f_x=(-x + (x**2+4)**(1/2))/((x**4+1)**(1/7))
if x > 0:
   print(f"gia tri can tim cua f(x)={f_x:.2f}")
else:
    print("Loi phep tinh")