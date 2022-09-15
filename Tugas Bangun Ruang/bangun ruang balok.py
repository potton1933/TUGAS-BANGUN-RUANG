print ("menghitung luas dan volume balok")

p=int(input("masukkan panjangnya = "))
l=int(input("masukkan lebarnya = "))
t=int(input("masukkan tingginya = "))

luas = (2*p*l)+(2*p*t)+(2*l*t)
volume = p*l*t

print("luas baloknya adalah = ",luas)
print("volume baloknya adalah = ",volume)