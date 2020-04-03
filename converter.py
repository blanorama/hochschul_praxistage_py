def convert(arg: int) -> str:
    res: str = ''
    cheat = [
        ('ↂ', 10000),
        ('ↁ', 5000),
        ('M', 1000),
        ('D', 500),
        ('C', 100),
        ('L', 50),
        ('X', 10),
        ('V', 5),
        ('I', 1)
    ]

    while arg > 0:
        for i in range(0, len(cheat)):
            if arg >= cheat[i][1]:
                if i is not 0 and arg is not cheat[i][1] and arg < cheat[i-1][1] and arg >= cheat[i-1][1] - cheat[i][1]:
                    res += cheat[i][0] + cheat[i-1][0]
                    arg -= cheat[i-1][1] - cheat[i][1]
                    break
                else:
                    res += cheat[i][0]
                    arg -= cheat[i][1]
    return res
