# def add(a, b):
#     """ Функция, которая складывает два числа"""
#     return  a + b

def mask_number(number: str, visible_start: int = 4, visible_end: int = 4, mask_char: str = '*') -> str:
    """
    Маскирует номер карты или счета.

    Args:
        number (str): Номер карты или счета для маскировки.
        visible_start (int): Количество видимых цифр с начала номера. По умолчанию 4.
        visible_end (int): Количество видимых цифр с конца номера. По умолчанию 4.
        mask_char (str): Символ, используемый для маскировки. По умолчанию '*'.

    Returns:
        str: Замаскированный номер.

    Raises:
        ValueError: Если номер слишком короткий для заданной маскировки
                    или если visible_start + visible_end превышает длину номера.
    """
    if not isinstance(number, str):
        raise TypeError("Номер должен быть строкой.")

    # Удаляем пробелы и тире, если они есть
    cleaned_number = number.replace(" ", "").replace("-", "")

    # Проверка на минимальную длину
    if len(cleaned_number) < visible_start + visible_end:
        raise ValueError(f"Номер слишком короткий ({len(cleaned_number)} символов) для маскировки с {visible_start} видимыми символами с начала и {visible_end} с конца.")

    # Формируем маскированную часть
    masked_part = mask_char * (len(cleaned_number) - visible_start - visible_end)

    # Собираем окончательный замаскированный номер
    masked_number = cleaned_number[:visible_start] + masked_part + cleaned_number[-visible_end:]

    return masked_number

# --- Примеры использования ---

# Маскировка номера банковской карты
card_number = "1234-5678-9012-3456"
masked_card = mask_number(card_number)
print(f"Оригинальный номер карты: {card_number}")
print(f"Замаскированный номер карты: {masked_card}") # Ожидаемый вывод: 1234********3456

# Маскировка номера счета с другими параметрами
account_number = "40817810100000001234"
masked_account = mask_number(account_number, visible_start=2, visible_end=2, mask_char='#')
print(f"\nОригинальный номер счета: {account_number}")
print(f"Замаскированный номер счета: {masked_account}") # Ожидаемый вывод: 40##############34

# Пример с слишком коротким номером (вызовет ошибку)
try:
    short_number = "123"
    mask_number(short_number)
except ValueError as e:
    print(f"\nОшибка при маскировке короткого номера: {e}")

# Пример с некорректным типом данных (вызовет ошибку)
try:
    invalid_input = 1234567890123456
    mask_number(invalid_input)
except TypeError as e:
    print(f"\nОшибка при маскировке некорректного типа данных: {e}")
