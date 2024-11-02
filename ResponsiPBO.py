class Produk:
    def __init__(self, kode_produk, nama_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

    def display_info(self):
        print(f"Kode Produk: {self.kode_produk}")
        print(f"Nama Produk: {self.nama_produk}")
        print(f"Harga: {self.harga}")


# Kelas Snack yang merupakan subclass dari Produk
class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, harga)

    def display_info(self):
        print("Kategori: Snack")
        super().display_info()


# Kelas Makanan yang merupakan subclass dari Produk
class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, harga)

    def display_info(self):
        print("Kategori: Makanan")
        super().display_info()


# Kelas Minuman yang merupakan subclass dari Produk
class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, harga)

    def display_info(self):
        print("Kategori: Minuman")
        super().display_info()


# Kelas Transaksi
class Transaksi:
    def __init__(self, no_transaksi, tanggal_transaksi, produk):
        self.no_transaksi = no_transaksi
        self.tanggal_transaksi = tanggal_transaksi
        self.produk = produk

    def display_transaksi(self):
        print(f"No Transaksi: {self.no_transaksi}")
        print(f"Tanggal Transaksi: {self.tanggal_transaksi}")
        self.produk.display_info()


# Daftar produk dan transaksi
produk_list = []
transaksi_list = []


# Fungsi untuk menambah produk
def tambah_produk():
    print("\n=== Tambah Produk ===")
    kategori = input("Masukkan kategori produk (Snack/Makanan/Minuman): ").strip().lower()
    kode = input("Masukkan kode produk: ")
    nama = input("Masukkan nama produk: ")
    harga = float(input("Masukkan harga produk: "))

    if kategori == "snack":
        produk = Snack(kode, nama, harga)
    elif kategori == "makanan":
        produk = Makanan(kode, nama, harga)
    elif kategori == "minuman":
        produk = Minuman(kode, nama, harga)
    else:
        print("Kategori tidak valid!")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")


# Fungsi untuk membuat transaksi
def buat_transaksi():
    print("\n=== Buat Transaksi ===")
    if not produk_list:
        print("Tidak ada produk yang tersedia. Tambahkan produk terlebih dahulu.")
        return

    no_transaksi = input("Masukkan nomor transaksi: ")
    tanggal = input("Masukkan tanggal transaksi (YYYY-MM-DD): ")

    print("\nDaftar Produk:")
    for idx, produk in enumerate(produk_list, 1):
        print(f"{idx}. {produk.nama_produk} - {produk.harga}")

    pilihan = int(input("Pilih produk berdasarkan nomor: ")) - 1
    if 0 <= pilihan < len(produk_list):
        produk = produk_list[pilihan]
        transaksi = Transaksi(no_transaksi, tanggal, produk)
        transaksi_list.append(transaksi)
        print("Transaksi berhasil dibuat!")
    else:
        print("Pilihan tidak valid!")


# Fungsi untuk menampilkan semua transaksi
def lihat_transaksi():
    print("\n=== Daftar Transaksi ===")
    if not transaksi_list:
        print("Belum ada transaksi.")
    else:
        for transaksi in transaksi_list:
            transaksi.display_transaksi()
            print("-----------------------")


# Menu utama
def menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Produk")
        print("2. Buat Transaksi")
        print("3. Lihat Daftar Transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            buat_transaksi()
        elif pilihan == "3":
            lihat_transaksi()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")


# Menjalankan program
if __name__ == "__main__":
    menu()
