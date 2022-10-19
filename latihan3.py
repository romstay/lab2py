# input nilai variable
a=input("masukkan nilai a:")
b=input("masukkan nilai b:")

# cetak nilai variable
print("variable a=",a)
print("variable b=",b)

# cetak hasil operasi kedua variable dengan string format
print("hasil penggabungan (1)+(0)=%s".format(a,b)%(a+b))

# konversi nilai variable
a=int(a)
b=int(b)
print("hasil penjumlahan (1)+(0)=%d".format(a,b)%(a+b))
print("hasil pembagian (1)/(0)=%d".format(a,b)%(a/b))
