import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка обмежень
    if min >= max or quantity <= 0 or quantity > (max - min + 1):
        return []
    
    # Генерація списку чисел від min до max
    numbers = list(range(min, max + 1))
    
    # Вибір випадкових чисел без повторень
    chosen_numbers = random.sample(numbers, k=quantity)

     # Сортування списку перед поверненням
    chosen_numbers.sort()
    return chosen_numbers

# Приклад використання
min = 1
max = 49
quantity = 6

ticket_numbers = get_numbers_ticket(min, max, quantity)
if ticket_numbers:
    print(f"Your ticket numbers are: {ticket_numbers}")
else:
    print("Invalid parameters")
