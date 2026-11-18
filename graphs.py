import matplotlib.pyplot as plt
import numpy as np

# 1. Ввод диапазона и шага с клавиатуры
# Если просто нажать Enter, берутся значения по заданию: от -3 до 3 с шагом 0.5
start = input("Начало диапазона (Enter = -3): ")
end = input("Конец диапазона (Enter = 3): ")
step = input("Шаг (Enter = 0.5): ")

start = float(start) if start else -3
end = float(end) if end else 3
step = float(step) if step else 0.5

# 2. Значения X от start до end включительно
x = np.arange(start, end + step / 2, step)

# 3. Значения Y для двух функций
y2 = x ** 2
y3 = x ** 3

# 4. Построение графиков
plt.figure(figsize=(8, 5))
plt.plot(x, y2, "b--o", label="y = x^2")  # синяя пунктирная линия с кружочками
plt.plot(x, y3, "r-s", label="y = x^3")   # красная сплошная линия с квадратиками

# 5. Оформление
plt.title("Графики функций y = x^2 и y = x^3")
plt.xlabel("Значения X")
plt.ylabel("Значения Y")
plt.grid(True)
plt.legend(loc="upper left")

# 6. Сохраняем картинку и показываем график
plt.savefig("graphs.png")
plt.show()
