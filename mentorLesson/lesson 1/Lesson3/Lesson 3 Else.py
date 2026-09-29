def restoran_bot(mesaj):
    mesaj=mesaj.lower()
    if "sifarish" in mesaj:
        return "Sifarishiniz qebul edildi"
    elif "menyu" in mesaj:
        return "Bugun plov, kabab, shorba"
    elif "qiymet" in mesaj:
        return "Orta chek 15 AZN-dir"
    elif "salam" in mesaj:
        return "Restoranimiza xosh geldiniz!"
    else:
        return "Basha dushmedim, yeniden yazin"

print(restoran_bot("Salam, masa sifarish etmek isteyirem "))
print(restoran_bot("Menyu nedir?"))
print(restoran_bot("Qiymetler neciyedir?"))
print(restoran_bot("Sabah aciqsiniz?"))
