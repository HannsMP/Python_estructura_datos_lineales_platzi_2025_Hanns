option_colors = {
    'reset': [0, 0],

    'bold': [1, 22],
    'dim': [2, 22],
    'italic': [3, 23],
    'underline': [4, 24],
    'inverse': [7, 27],
    'hidden': [8, 28],
    'strikethrough': [9, 29],

    'black': [30, 39],
    'red': [31, 39],
    'green': [32, 39],
    'yellow': [33, 39],
    'blue': [34, 39],
    'magenta': [35, 39],
    'cyan': [36, 39],
    'white': [37, 39],
    'gray': [90, 39],
    'grey': [90, 39],

    'brightRed': [91, 39],
    'brightGreen': [92, 39],
    'brightYellow': [93, 39],
    'brightBlue': [94, 39],
    'brightMagenta': [95, 39],
    'brightCyan': [96, 39],
    'brightWhite': [97, 39],

    'bgBlack': [40, 49],
    'bgRed': [41, 49],
    'bgGreen': [42, 49],
    'bgYellow': [43, 49],
    'bgBlue': [44, 49],
    'bgMagenta': [45, 49],
    'bgCyan': [46, 49],
    'bgWhite': [47, 49],
    'bgGray': [100, 49],
    'bgGrey': [100, 49],

    'bgBrightRed': [101, 49],
    'bgBrightGreen': [102, 49],
    'bgBrightYellow': [103, 49],
    'bgBrightBlue': [104, 49],
    'bgBrightMagenta': [105, 49],
    'bgBrightCyan': [106, 49],
    'bgBrightWhite': [107, 49],

    'blackBG': [40, 49],
    'redBG': [41, 49],
    'greenBG': [42, 49],
    'yellowBG': [43, 49],
    'blueBG': [44, 49],
    'magentaBG': [45, 49],
    'cyanBG': [46, 49],
    'whiteBG': [47, 49],
}

def colors(color:str, *text:str):
    open_code, close_code = option_colors.get(color, option_colors['reset'])
    return f"\u001b[{open_code}m{' '.join(text)}\u001b[{close_code}m"

print(colors('brightYellow', '[]'))
print(colors('brightMagenta', '[]'))
print(colors('brightCyan', '[]'))