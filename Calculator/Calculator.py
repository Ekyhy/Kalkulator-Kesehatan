def run_program():


    print("Selamat Datang di Kalkulator Kesehatan")
    print("Pilih Opsi")
    print("(1) Hitung Berat Badan Ideal")
    print("(2) Hitung Potensial Tinggi Genetik")

    operate = input("masukkan opsi :")

    if operate == "1":
        angka1 = int(input("Tinggi Badan Anda : "))
        hitung1 = angka1 - 100
        hitung2 = hitung1*0.10
        result = hitung1-hitung2
        print("Berat Badan Ideal Anda")
        print(result)
    if operate == "2":
        angka1 = int(input("Tinggi Badan Ayah : "))
        angka2 = int(input("Tinggi Badan Ibu : "))
        hitung1 = angka1+angka2+13
        result = hitung1/2
        print("Tinggi Badan Potensial Genetik Anda")
        print (result)

    


while True:
    run_program()
    pilihan = input("Apakah ingin menjalankan lagi?y (y/n): ").lower()
    if pilihan != 'y':
        print("Program selesai.")
        break
