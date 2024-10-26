class Order:
    def __init__(self, ID, name, details):
        self.__ID = ID  # Private attribute
        self.name = name  # Public attribute
        self.details = details  # Public attribute
        self.deliveries = []  # List to store associated Delivery objects

    def setOrder(self):
        print(f"Pesanan '{self.name}' diatur dengan rincian: {self.details}")

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)
        print(f"Pengiriman '{delivery.name}' ditambahkan ke Pesanan '{self.name}'")

    def show_deliveries(self):
        print(f"Daftar pengiriman untuk Pesanan '{self.name}':")
        for delivery in self.deliveries:
            print(f"  - {delivery.name} pada tanggal {delivery.date} ke alamat {delivery.address}")

    def get_ID(self):
        return self.__ID


class Delivery:
    def __init__(self, id, name, information, date, address):
        self.__id = id  # Private attribute
        self.name = name  # Public attribute
        self.information = information  # Public attribute
        self.date = date  # Public attribute
        self.address = address  # Public attribute

    def processDelivery(self):
        print(f"Memproses pengiriman '{self.name}' untuk alamat: {self.address} pada tanggal {self.date}")

    def get_id(self):
        return self.__id


class OrderSystem:
    def __init__(self):
        self.orders = {}  # Dictionary to store orders with ID as key

    def create_order(self):
        order_id = int(input("Masukkan ID Pesanan: "))
        name = input("Masukkan Nama Pesanan: ")
        details = input("Masukkan Rincian Pesanan: ")
        order = Order(order_id, name, details)
        self.orders[order_id] = order
        print(f"Pesanan '{name}' berhasil dibuat.")

    def add_delivery_to_order(self):
        order_id = int(input("Masukkan ID Pesanan: "))
        if order_id in self.orders:
            name = input("Masukkan Nama Pengiriman: ")
            information = input("Masukkan Informasi Pengiriman: ")
            date = input("Masukkan Tanggal Pengiriman (YYYY-MM-DD): ")
            address = input("Masukkan Alamat Pengiriman: ")
            delivery = Delivery(len(self.orders[order_id].deliveries) + 1, name, information, date, address)
            self.orders[order_id].add_delivery(delivery)
            print(f"Pengiriman '{name}' berhasil ditambahkan ke Pesanan ID {order_id}.")
        else:
            print("Pesanan tidak ditemukan.")

    def show_all_orders(self):
        if not self.orders:
            print("Belum ada pesanan.")
        else:
            for order in self.orders.values():
                print(f"\nPesanan ID: {order.get_ID()}")
                print(f"Nama: {order.name}")
                print(f"Rincian: {order.details}")
                order.show_deliveries()

    def process_deliveries(self):
        order_id = int(input("Masukkan ID Pesanan untuk memproses pengiriman: "))
        if order_id in self.orders:
            order = self.orders[order_id]
            for delivery in order.deliveries:
                delivery.processDelivery()
        else:
            print("Pesanan tidak ditemukan.")

    def menu(self):
        while True:
            print("\n=== Sistem Manajemen Pesanan ===")
            print("1. Buat Pesanan Baru")
            print("2. Tambahkan Pengiriman ke Pesanan")
            print("3. Tampilkan Semua Pesanan dan Pengiriman")
            print("4. Proses Pengiriman pada Pesanan")
            print("5. Keluar")
            choice = input("Pilih opsi: ")

            if choice == "1":
                self.create_order()
            elif choice == "2":
                self.add_delivery_to_order()
            elif choice == "3":
                self.show_all_orders()
            elif choice == "4":
                self.process_deliveries()
            elif choice == "5":
                print("Keluar dari program.")
                break
            else:
                print("Opsi tidak valid. Silakan coba lagi.")


# Menjalankan program
if __name__ == "__main__":
    order_system = OrderSystem()
    order_system.menu()
