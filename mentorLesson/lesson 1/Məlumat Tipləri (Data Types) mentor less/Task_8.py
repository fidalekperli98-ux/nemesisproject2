qiymet = float(input("Mehsulun qiymetini yazin:"))
endirim = float(input("Endirim faizini yazin:"))
qiymet -=qiymet * endirim / 100
print("Endirimli qiymet", qiymet)

