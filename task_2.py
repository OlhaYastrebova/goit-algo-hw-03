import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка обмежень
    if min_num >= max_num or quantity <= 0 or quantity > (max_num - min_num + 1):
        return []
    
    # Генерація списку чисел від min до max
    numbers = list(range(min_num, max_num + 1))
    
    # Вибір випадкових чисел без повторень
    chosen_numbers = random.sample(numbers, k=quantity)

     # Сортування списку перед поверненням
    chosen_numbers.sort()
    return chosen_numbers

# Приклад використання
min_num = 1
max_num = 49
quantity = 6

ticket_numbers = get_numbers_ticket(min_num, max_num, quantity)
if ticket_numbers:
    print(f"Your ticket numbers are: {ticket_numbers}")
else:
    print("Invalid parameters")
