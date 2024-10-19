class Music:
    def __init__(self, title, singer, genre):
        self.title = title
        self.singer = singer
        self.genre = genre

    def display(self):
        return f"{self.title:<20} {self.singer:<20} {self.genre:<10}"

class MusicManager:
    def __init__(self):
        self.music_list = []

    def add_music(self, music):
        self.music_list.append(music)

    def delete_music(self, title):
        for music in self.music_list:
            if music.title.lower() == title.lower():
                self.music_list.remove(music)
                print(f"'{title}' Berhasil dihapus.")
                return
        print(f"'{title}' tidak ditemukan.")

    def display_by_genre(self, genre_filter):
        filtered_music = [music for music in self.music_list if music.genre.lower() == genre_filter.lower()]
        if filtered_music:
            print(f"\n{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
            print("-" * 50)
            for music in filtered_music:
                print(music.display())
        else:
            print(f"tidak ada music yang di temukan untuk genre: {genre_filter}")

    def search_by_artist(self, artist_name):
        found_music = [music for music in self.music_list if music.singer.lower() == artist_name.lower()]
        if found_music:
            print(f"\nSongs by {artist_name}:")
            print(f"\n{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
            print("-" * 50)
            for music in found_music:
                print(music.display())
        else:
            print(f"No songs found by artist: {artist_name}")

    def search_by_title(self, title):
        found_music = [music for music in self.music_list if music.title.lower() == title.lower()]
        if found_music:
            print(f"\n{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
            print("-" * 50)
            for music in found_music:
                print(music.display())

        else:
             print(f"No songs found with title: {title}")
                
    def display_all_music(self):
        if not self.music_list:
            print("Tidak ada music tersedia.")
        else:
            print(f"\n{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
            print("-" * 50)
            for music in self.music_list:
                print(music.display())

def menu():
    manager = MusicManager()

    manager.add_music(Music("Down Bad", "J. Cole", "Rap"))
    manager.add_music(Music("BLOOD", "Kendrick Lamar", "Hip Hop"))
    manager.add_music(Music("Love Galore", "SZA", "R&B"))
    manager.add_music(Music("Blinding Lights", "The Weeknd", "R&B"))
    manager.add_music(Music("Lose Yourself", "Eminem", "Rap"))
    manager.add_music(Music("HUMBLE.", "Kendrick Lamar", "Rap"))
    manager.add_music(Music("Crazy in Love", "Beyoncé", "R&B"))
    manager.add_music(Music("No Role Modelz", "J. Cole", "Hip Hop"))
    manager.add_music(Music("Money Trees", "Kendrick Lamar", "Hip Hop"))
    manager.add_music(Music("All of Me", "John Legend", "R&B"))
    manager.add_music(Music("Not Afraid", "Eminem", "Rap"))
    manager.add_music(Music("DNA.", "Kendrick Lamar", "Rap"))
    manager.add_music(Music("Hurricane", "Kanye West", "Hip Hop"))
    manager.add_music(Music("Wet Dreamz", "J. Cole", "Hip Hop"))
    manager.add_music(Music("Riggamortis", "Kendrick Lamar", "Hip Hop"))
    manager.add_music(Music("King Kunta", "Kendrick Lamar", "Hip Hop"))
    manager.add_music(Music("Ex Factor", "Ms. Lauryn Hill", "R&B"))


    while True:
        print("\n--- Music Manager Menu ---")
        print("1. Tambahkan musik baru")
        print("2. Hapus Musik")
        print("3. Tampilkan Genre (Rap, R&B, Hip Hop)")
        print("4. Tampilkan Semua Musik")
        print("5. Cari Berdasarkan Artis")
        print("6. Cari Berdasarkan Judul")
        print("0. Exit")

        choice = input("Masukan Pilihan Menu : ")

        if choice == '1':
            title = input("Masukkan Judul: ")
            singer = input("Masukkan Penyanyi: ")
            genre = input("Masukkan Genre(Rap/R&B/Hip Hop): ")
            manager.add_music(Music(title, singer, genre))
            print(f"Music '{title}' by {singer} added to {genre} genre.")
        
        elif choice == '2':
            title = input("Masukkan Judul lagu Yang akan dihapus: ")
            manager.delete_music(title)

        elif choice == '3':
            genre = input("Masukkan genre yang ingin ditampilkan (Rap/R&B/Hip Hop): ")
            manager.display_by_genre(genre)

        elif choice == '4':
            manager.display_all_music()

        elif choice == "5":
            Artist_name = input("Masukkan Nama Artis yang ingin Anda cari: ")
            manager.search_by_artist(Artist_name)

        elif choice == '6':
            title = input("Enter song title to search: ")
            manager.search_by_title(title)

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Pilihan salah, Mohon Coba lagi.")

# Running the menu
if __name__ == "__main__":
    menu()