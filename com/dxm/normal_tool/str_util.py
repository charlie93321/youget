def is_empty(str1: str):
    if str1 is None:
        return True
    elif str1.strip() == '':
        return True
    else:
        return False


def is_not_empty(str1: str):
    return not is_empty(str1)
