import random

class OrderDataHelper:
    @staticmethod
    def generate_order_data():
        names = ["Иван", "Ян", "Константин", "Ли", "Александр", "Анна", "Дмитрий", "Мария"]
        surnames = ["Иванов", "Петрова", "Сидоров", "Кузнецова", "Смирнов", "Попова", "Васильев", "Соколова"]
        name = random.choice(names)
        surname = random.choice(surnames)
        address = f"Москва, ул. Софийская набережная, д. {random.randint(100, 200)}"
        telephone = f"79{random.randint(100000000, 999999999)}"
        date = f"{random.randint(10, 28)}.{random.randint(10, 12)}.2026"
        comment = "Тестовый комментарий"
        return name, surname, address, telephone, date, comment