import pulp

# Створюємо задачу лінійного програмування для максимізації (LP Maximize problem)
model = pulp.LpProblem("Drink_Production_Optimization", pulp.LpMaximize)

# Визначаємо змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Функція мети: максимізація загальної кількості продуктів
model += lemonade + fruit_juice, "Total Products"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar Constraint"
model += 1 * lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal number of Lemonade to produce: {pulp.value(lemonade)}")
print(f"Optimal number of Fruit Juice to produce: {pulp.value(fruit_juice)}")
