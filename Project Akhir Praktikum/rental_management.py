class Car:
    def __init__(self, car_id, brand, model, year, daily_rate, available=True):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.available = available

class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, car_id, rental_duration):
        # Mencari mobil berdasarkan ID
        car = next((c for c in self.cars if c.car_id == car_id), None)

        # Nested if pertama: Memeriksa apakah mobil ditemukan
        if car:
            # Nested if kedua: Memeriksa apakah mobil tersedia untuk disewa
            if car.available:
                car.available = False
                total_cost = car.daily_rate * rental_duration
                return f'Sukses menyewa {car.brand} {car.model} ({car.year}) untuk {rental_duration} hari. Biaya total: Rp{total_cost}.'
            else:
                return 'Mobil tidak tersedia.'
        else:
            return 'Mobil tidak ditemukan.'

    def display_available_cars(self):
        print("Mobil yang Tersedia:")
        for car in self.cars:
            if car.available:
                print(f'ID: {car.car_id}, Merk: {car.brand}, Model: {car.model}, Tahun: {car.year}, Harga/Hari:{car.daily_rate}')
