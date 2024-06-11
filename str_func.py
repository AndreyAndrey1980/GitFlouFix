def to_uppercase(s: str) -> str:
    """ Может они не увидели его ...
    Преобразует все символы в строке s в верхний регистр и возвращает результат.

    :param s: Строка для преобразования.
    :return: Строка с всеми символами в верхнем регистре.
    """
    return s.upper()

input_string = "привет, мир. как дела?"
uppercased_string = to_uppercase(input_string)
print(uppercased_string)

capitalized_string = capitalize_words(input_string)
print(capitalized_string)