def convert(arg: int) -> str:
    res: str = '';
    while (arg > 0):
        res += 'I'
        arg-=1
    return res
