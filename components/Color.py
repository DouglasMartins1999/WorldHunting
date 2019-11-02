def toRGB(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

level_colors = [
    "#999999",
    "#D44242",
    "#D4B942",
    "#88D562",
    "#63C9D6",
    "#B363D6"
]