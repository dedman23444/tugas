def apakah_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

def tampilkan_angka_prima(awal, akhir):
    prima = []
    for angka in range(awal, akhir + 1):
        if apakah_prima(angka):
            prima.append(angka)
    return prima

def tampilkan_angka_ganjil(awal, akhir):
    return [angka for angka in range(awal, akhir + 1) if angka % 2 != 0]

def tampilkan_angka_genap(awal, akhir):
    return [angka for angka in range(awal, akhir + 1) if angka % 2 == 0]

def menu():
    while True:
        print("\nMenu:")
        print("1. Tampilkan Angka Prima")
        print("2. Tampilkan Angka Ganjil")
        print("3. Tampilkan Angka Genap")
        print("4. Keluar dari Sistem")
        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == '1':
            awal = int(input("Masukkan batas awal untuk angka prima: "))
            akhir = int(input("Masukkan batas akhir untuk angka prima: "))
            prima = tampilkan_angka_prima(awal, akhir)
            print(f"Angka prima dari {awal} hingga {akhir}: {prima}")

        elif pilihan == '2':
            awal = int(input("Masukkan batas awal untuk angka ganjil: "))
            akhir = int(input("Masukkan batas akhir untuk angka ganjil: "))
            ganjil = tampilkan_angka_ganjil(awal, akhir)
            print(f"Angka ganjil dari {awal} hingga {akhir}: {ganjil}")

        elif pilihan == '3':
            awal = int(input("Masukkan batas awal untuk angka genap: "))
            akhir = int(input("Masukkan batas akhir untuk angka genap: "))
            genap = tampilkan_angka_genap(awal, akhir)
            print(f"Angka genap dari {awal} hingga {akhir}: {genap}")

        elif pilihan == '4':
            print("Program Selesai bye bye!")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih lagi.")

# Jalankan fungsi menu
menu()