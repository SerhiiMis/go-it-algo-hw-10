import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок для методу Монте-Карло
N = 10000

# Обчислення інтеграла методом Монте-Карло
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_monte_carlo = (b - a) * np.mean(y_random)

# Обчислення інтеграла аналітично за допомогою функції quad
result, error = spi.quad(f, a, b)

# Виведення результатів
print(f"Значення інтеграла за методом Монте-Карло: {integral_monte_carlo}")
print(f"Аналітичне значення інтеграла: {result}")
print(f"Абсолютна похибка методу Монте-Карло: {abs(integral_monte_carlo - result)}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Відображення точок Монте-Карло
ax.scatter(x_random, y_random, color='blue', s=5, alpha=0.5)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
