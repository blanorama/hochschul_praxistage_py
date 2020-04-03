def convert(arg: int) -> str:
    res: str = ''
    cheat = {
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    while arg > 0:
        for key, value in cheat.items():
            if (arg >= value):
                res += key
                arg -= value
                break
    return res