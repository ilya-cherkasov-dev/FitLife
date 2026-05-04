# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000


# 1. Знакомство
user_name = input("Введите ваше имя: ").strip()

try:
    user_age = int(input("Введите ваш возраст: "))
except ValueError:
    print("Ошибка: возраст должен быть числом.")
    user_age = 0


# 2. Сбор данных
try:
    user_weight = float(input("Введите вес (кг): "))
    user_height = float(input("Введите рост (в метрах, например 1.75): "))
except ValueError:
    print("Ошибка: вес и рост должны быть числами.")
    user_weight = 0.0
    user_height = 1.0


# 3. Логика расчетов
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл, переводим в литры
water_l = (user_weight * WATER_PER_KG) / ML_IN_LITER


# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
