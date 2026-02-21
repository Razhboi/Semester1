from rental_management import Car, RentalSystem

def main():
    # Inisialisasi sistem penyewaan
    rental_system = RentalSystem()

    # Menambahkan beberapa mobil dengan harga sewa harian yang acak
    rental_system.add_car(Car(1, "Toyota", "Avanza", 2022, 150000))
    rental_system.add_car(Car(2, "Honda", "Civic", 2021, 300000))
    rental_system.add_car(Car(3, "Mitsubishi", "Expander", 2020, 200000))
    rental_system.add_car(Car(4, "Daihatsu", "Xenia", 2022, 150000))
    rental_system.add_car(Car(5, "Honda", "Jazz", 2021, 100000))
    rental_system.add_car(Car(6, "Toyota", "Kijang Inova Reborn", 2020, 350000))

    while True:
        # Menampilkan menu
        print("\nMenu:")
        print("1. Tampilkan Mobil yang Tersedia")
        print("2. Sewa Mobil")
        print("3. Keluar")

        choice = input("Pilih menu (1/2/3): ")

        if choice == '1':
            # Menampilkan mobil yang tersedia
            rental_system.display_available_cars()
        elif choice == '2':
            # Meminta input ID mobil untuk disewa
            car_id_to_rent = int(input("Masukkan ID mobil yang ingin Anda sewa: "))
            rental_duration = int(input("Masukkan durasi sewa (hari): "))
            result = rental_system.rent_car(car_id_to_rent, rental_duration)
            print(result)
        elif choice == '3':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()