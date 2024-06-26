import re

phone_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone):
    # Видалення всіх нецифрових символів
    phone = re.sub(r'\D', '', phone)
    
    # Додавання коду країни, якщо його немає
    if phone.startswith('380'):
        phone = '+' + phone
    elif phone.startswith('0'):
        phone = '+38' + phone
    
    return phone

# Застосування функції до списку номерів
sanitized_numbers = [normalize_phone(phone) for phone in phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)