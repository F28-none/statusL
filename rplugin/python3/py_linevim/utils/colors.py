#mendefiniikan dan membuat configurasi color
def send_color(bg='#000000',fg='#ffffff',font='bold'):
    return f'guibg={bg} guifg={fg} gui={font}'

#mngubah warna di setiao masing masing mode
def get_color_mode(mode,mode_theme):
        return mode_theme.get(mode,'#000000')
