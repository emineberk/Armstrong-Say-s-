sayi = int(input("Bir sayı giriniz: "))

toplam = 0
sayi1=sayi
sayibasamak = len(str(sayi))

while sayi1>0 :
        basamak = sayi1 % 10
        toplam += basamak ** sayibasamak
        sayi1//=10
        
if toplam == sayi:
    print("{} sayısı bir Armstrong sayısıdır.".format(sayi))
    
else:
    print("{} sayısı bir Armstrong sayısı değildir.".format(sayi))