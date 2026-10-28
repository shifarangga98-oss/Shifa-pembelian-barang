print("=== PROGRAM PEMBELIAN BARANG ===")

harga = int(input("Masukkan harga barang: "))
uang = int(input("Masukkan jumlah uang: "))

if uang >= harga and harga > 0:
    print("Pembelian berhasil")
    print("Kembalian:", uang - harga)
else:
    print("Pembelian gagal, uang tidak cukup atau harga tidak valid")