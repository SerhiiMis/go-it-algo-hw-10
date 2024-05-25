Висновки
1.Метод Монте-Карло:
    -Ми використовували 10,000 випадкових зразків для оцінки інтеграла.
    -Обчислений інтеграл методом Монте-Карло близький до аналітичного значення, але може мати деяку похибку залежно від кількості зразків.

2.Аналітичне обчислення та функція quad:
    -Інтеграл аналітично дорівнює 8/3 ≈ 2.6667
    -Функція quad з SciPy повертає значення 2.666666666666667, що є дуже точним.

Порівняння:
    -Похибка методу Монте-Карло зменшується зі збільшенням кількості зразків, але все ще може відрізнятися від аналітичного значення через випадковість вибору точок.
    -Метод Монте-Карло є корисним для задач, де аналітичне обчислення є складним або неможливим.

Виведення
    Метод Монте-Карло є надійним чисельним методом для оцінки інтегралів, особливо при великій кількості зразків. Однак для задач з простою аналітичною формулою, як у нашому випадку, методи на кшталт функції quad з SciPy надають більш точні результати з мінімальною похибкою.