#Istifadechiden melumatlari aliriq
ad=input("Adinizi daxil edin: ")
yash=int(input("Yashinizi daxil edin: "))
gelir=float(input("Gelirinizi daxil edin: "))

     #hesablamalar
dogum_ili = 2026 -yash
vergi=gelir * 0.20
xalis_gelir=gelir - vergi



print(f"ad {ad}")
print(f"yash {yash}")
print(f"gelir {gelir}")
print(f"dogum ili {dogum_ili}" )
print(f"vergi (20%)  {vergi:.2f} AZN")
print(f"xalis gelir : {xalis_gelir} AZN")







