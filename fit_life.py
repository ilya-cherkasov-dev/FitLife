# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000


# 1. Знакомство
user_name = input("Введите ваше имя: ").strip()

try:
    user_age = int(input("Введите ваш возраст: "))
except ValueError:
    raise ValueError("Ошибка: возраст должен быть целым числом.")


# 2. Сбор данных
try:
    user_weight = float(input("Введите вес (кг): "))
except ValueError:
    raise ValueError("Ошибка: вес должен быть числом, например 75.5")

try:
    user_height = float(input("Введите рост (в метрах, например 1.75): "))
except ValueError:
    raise ValueError("Ошибка: рост должен быть числом, например 1.75")


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
