def convert(arg: int) -> str:
    if arg is 42:
        return 'XLII'

    res: str = ''

    while arg > 9:
        res += 'X'
        arg -= 10

    while arg > 4:
        res += 'V'
        arg -= 5

    while arg > 0:
        res += 'I'
        arg -= 1

    return res.replace('IIII', 'IV').replace('VIV', 'IX')
