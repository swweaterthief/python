import re

def is_valid_password(password):
    """
    Функция проверяет корректность пароля.

    Args:
        password (str): Пароль для проверки.

    Returns:
        bool: True если пароль корректный, иначе False.

    Doctest:
        >>> is_valid_password('rtG3FG!Tr^e')
        True
        >>> is_valid_password('aA1!*!1Aa')
        True
        >>> is_valid_password('oF^a1D@y5e6')
        True
        >>> is_valid_password('enroi#$rkdeR#$092uWedchf34tguv394h')
        True
        >>> is_valid_password('пароль')
        False
        >>> is_valid_password('password')
        False
        >>> is_valid_password('qwerty')
        False
        >>> is_valid_password('lOngPa$$$W0Rd')
        False
    """

    if len(password) < 6:
        return False


    if not re.fullmatch(r'[A-Za-z0-9^$%@#&*!?]*', password):
        return False


    if len(re.findall(r'[A-Z]', password)) < 2:
        return False


    if not re.search(r'\d', password):
        return False


    if len(set(re.findall(r'[\^$%@#&*!?]', password))) < 2:
        return False

    
    if re.search(r'(.)\1\1', password):
        return False

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()