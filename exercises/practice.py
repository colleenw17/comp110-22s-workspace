    """Seeing how many times a color appears (as a value)."""
    color: dict[str, int] = {}
    empty: str = ""
    max: int = 0
    for x in popular:
        if popular[x] in color:
            color[x] += 1
        else:
            color[x] = 1
    for y in color:
        if color[y] > max:
            max = color[y]
            empty = y 
        else:
            if color[y] == max:
                empty = y[1]
    return empty     