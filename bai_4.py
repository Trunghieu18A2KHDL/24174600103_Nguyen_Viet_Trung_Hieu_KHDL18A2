t = int(input("nhap thoi gian su dung bong den"))
if t < 0:
    print("Thoi gian phai lon hon 0")
else:
  hieu_dien_the = 220
  cuong_do_dong_dien = 2.7
  cong_suat = t*hieu_dien_the*cuong_do_dong_dien/3600*1000
  tien_phai_tra = cong_suat*7000
print(f"tien phai tra: {tien_phai_tra}")


    
    
