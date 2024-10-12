class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama
        self.ktp = ktp
        self.limit_pinjaman = int(limit_pinjaman)

class Pinjaman:
    def __init__(self, debitur, jumlah_pinjaman, bunga, bulan):
        self.debitur = debitur
        self.jumlah_pinjaman = int(jumlah_pinjaman)
        self.bunga = float(bunga)
        self.bulan = int(bulan)

    def hitung_angsuran(self):
        angsuran_pokok = self.jumlah_pinjaman * (self.bunga / 100)
        angsuran_bulanan = angsuran_pokok / self.bulan
        total_angsuran = angsuran_pokok + angsuran_bulanan

        return angsuran_pokok, angsuran_bulanan, total_angsuran

    def tampilkan_perhitungan_angsuran(self):
        angsuran_pokok, angsuran_bulanan, total_angsuran = self.hitung_angsuran()

        print("\n================= Perhitungan Angsuran =================")
        print(f"Nama Debitur    : {self.debitur.nama}")
        print(f"Jumlah Pinjaman : Rp.{self.jumlah_pinjaman:,}")
        print(f"Bunga           : {self.bunga}%")
        print(f"Durasi Pinjaman : {self.bulan} bulan")
        print(f"\nAngsuran Pokok  : Rp.{angsuran_pokok:,}")
        print(f"Angsuran Bulanan: Rp.{angsuran_bulanan:,} / bulan")
        print(f"Total Angsuran  : Rp.{total_angsuran:,}")
        print("=" * 60)

class SistemPinjaman:
    def __init__(self):
        self.debitur_list = []
        self.pinjaman_list = []

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        debitur_baru = Debitur(nama, ktp, limit_pinjaman)
        self.debitur_list.append(debitur_baru)
        print("Debitur berhasil ditambahkan.")

    def cari_debitur(self, nama):
        for debitur in self.debitur_list:
            if debitur.nama.lower() == nama.lower():
                return debitur
        return None

    def tampilkan_semua_debitur(self):
        print("\n================= Daftar Semua Debitur =================")
        if not self.debitur_list:
            print("Tidak ada debitur yang terdaftar.")
        else:
            print(f"{'Nama Debitur'.ljust(20)}{'No KTP'.ljust(20)}{'Limit Pinjaman'.ljust(20)}")
            print("=" * 60)

            for debitur in self.debitur_list:
                print(f"{debitur.nama.ljust(20)}{debitur.ktp.ljust(20)}Rp.{debitur.limit_pinjaman:,}".ljust(20))
            print("=" * 60)

    def tambah_pinjaman(self, nama, jumlah_pinjaman, bunga, bulan):
        debitur = self.cari_debitur(nama)
        if debitur:
            if int(jumlah_pinjaman) > debitur.limit_pinjaman:
                print("Pinjaman gagal: Jumlah pinjaman melebihi limit!")
            else:
                pinjaman_baru = Pinjaman(debitur, jumlah_pinjaman, bunga, bulan)
                self.pinjaman_list.append(pinjaman_baru)
                print("Pinjaman berhasil ditambahkan.")
        else:
            print("Debitur tidak ditemukan! Pinjaman gagal ditambahkan.")

    def tampilkan_semua_pinjaman(self):
        print("\n================= Daftar Semua Pinjaman =================")
        if not self.pinjaman_list:
            print("Tidak ada pinjaman yang terdaftar.")
        else:
            print(f"{'Nama Debitur'.ljust(20)}{'Jumlah Pinjaman'.ljust(20)}{'Bunga'.ljust(10)}{'Bulan'.ljust(10)}")
            print("=" * 60)

        for pinjaman in self.pinjaman_list:
                print(f"{pinjaman.debitur.nama.ljust(20)}Rp.{pinjaman.jumlah_pinjaman:,}".ljust(25) + f"{pinjaman.bunga:.2f}%".ljust(10) + f"{pinjaman.bulan}".ljust(10))
                print("=" * 60)
    def menu_kelola_debitur(self):
        while True:
            print("\n================ Kelola Debitur ================")
            print("1. Tampilkan Semua Debitur")
            print("2. Cari Debitur")
            print("3. Tambah Debitur")
            print("0. Kembali")
            pilihan = input("Masukan Pilihan Sub Menu: ")

            if pilihan == "1":
                self.tampilkan_semua_debitur()
            elif pilihan == "2":
                nama = input("\n>>> Cari Debitur\nMasukan Nama Debitur yg Ingin Di Cari: ")
                debitur = self.cari_debitur(nama)
                if debitur:
                    print(f"Nama Debitur    : {debitur.nama}")
                    print(f"No KTP          : {debitur.ktp}")
                    print(f"Limit Pinjaman  : Rp.{debitur.limit_pinjaman:,}")
                else:
                    print("Debitur tidak ditemukan!")
            elif pilihan == "3":
                nama = input("Masukkan nama debitur: ")
                ktp = input("Masukkan KTP debitur: ")
                limit_pinjaman = input("Masukkan limit pinjaman: Rp.")
                self.tambah_debitur(nama, ktp, limit_pinjaman)
            elif pilihan == "0":
                print("Kembali ke menu utama.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def menu_kelola_pinjaman(self):
        while True:
            print("\n================ Kelola Pinjaman ================")
            print("1. Tampilkan Semua Pinjaman")
            print("2. Cari Pinjaman")
            print("3. Tambah Pinjaman")
            print("4. Hitung Angsuran")
            print("0. Kembali")
            pilihan = input("Masukan Pilihan Sub Menu: ")

            if pilihan == "1":
                self.tampilkan_semua_pinjaman()
            elif pilihan == "2":
                nama = input("\n>>> Cari Pinjaman\nMasukan Nama Debitur yg Ingin Di Cari: ")
                for pinjaman in self.pinjaman_list:
                    if pinjaman.debitur.nama.lower() == nama.lower():
                        print(f"Nama Debitur    : {pinjaman.debitur.nama}")
                        print(f"Jumlah Pinjaman : Rp.{pinjaman.jumlah_pinjaman:,}")
                        print(f"Bunga           : {pinjaman.bunga}%")
                        print(f"Durasi Pinjaman : {pinjaman.bulan} bulan")
                        break
                else:
                    print("Pinjaman tidak ditemukan!")
            elif pilihan == "3":
                nama = input("Masukkan nama debitur: ")
                jumlah_pinjaman = input("Masukkan jumlah pinjaman: Rp.")
                bunga = input("Masukkan bunga pinjaman (%): ")
                bulan = input("Masukkan durasi pinjaman (bulan): ")
                self.tambah_pinjaman(nama, jumlah_pinjaman, bunga, bulan)
            elif pilihan == "4":
                nama = input("\n>>> Hitung Angsuran\nMasukan Nama Debitur untuk Hitung Angsuran: ")
                for pinjaman in self.pinjaman_list:
                    if pinjaman.debitur.nama.lower() == nama.lower():
                        pinjaman.tampilkan_perhitungan_angsuran()
                        break
                else:
                    print("Pinjaman tidak ditemukan!")
            elif pilihan == "0":
                print("Kembali ke menu utama.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def menu_utama(self):
        while True:
            print("\n================ Menu Utama ================")
            print("1. Kelola Debitur")
            print("2. Kelola Pinjaman")
            print("0. Keluar")
            pilihan = input("Masukan Pilihan Menu: ")

            if pilihan == "1":
                self.menu_kelola_debitur()
            elif pilihan == "2":
                self.menu_kelola_pinjaman()
            elif pilihan == "0":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    sistem_pinjaman = SistemPinjaman()
    sistem_pinjaman.menu_utama()