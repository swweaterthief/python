import re

def is_valid_color(color):
    """
    Функция проверяет корректность web цвета.

    Args:
        color (str): Цвет для проверки.

    Returns:
        bool: True если цвет корректный, иначе False.

    Doctest:
        >>> is_valid_color('#21f48D')
        True
        >>> is_valid_color('#888')
        True
        >>> is_valid_color('rgb(255, 255, 255)')
        True
        >>> is_valid_color('rgb(10%, 20%, 0%)')
        True
        >>> is_valid_color('hsl(200, 100%, 50%)')
        True
        >>> is_valid_color('hsl(0, 0%, 0%)')
        True
        >>> is_valid_color('#2345')
        False
        >>> is_valid_color('ffffff')
        False
        >>> is_valid_color('rgb(257, 50, 10)')
        False
        >>> is_valid_color('hsl(20, 10, 0.5)')
        False
        >>> is_valid_color('hsl(34%, 20%, 50%)')
        False
    """

    if re.fullmatch(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}', color):
        return True


    if re.fullmatch(r'rgb\((\d{1,2}|1\d\d|2[0-4]\d|25[0-5]), (\d{1,2}|1\d\d|2[0-4]\d|25[0-5]), (\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\)', color) or \
       re.fullmatch(r'rgb\((\d{1,2}%|100%), (\d{1,2}%|100%), (\d{1,2}%|100%)\)', color):
        return True


    if re.fullmatch(r'hsl\((\d{1,2}|[1-2]\d{2}|3[0-5]\d|360), (\d{1,2}%|100%), (\d{1,2}%|100%)\)', color):
        return True

    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()