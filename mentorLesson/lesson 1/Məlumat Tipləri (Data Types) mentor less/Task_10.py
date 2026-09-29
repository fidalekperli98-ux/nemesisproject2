istifadeci_adi = input("Istifadeci adini daxil edin:")
shifre = input("Shifreni daxil edin:")
girish_ugurlu = istifadeci_adi == "admin" and  shifre == "1234"
print("Girish_ugurlu:", girish_ugurlu)
print("Girish_ugursuz:" , not girish_ugurlu)

