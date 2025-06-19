def apply_color(bg='#000000',fg='#ffffff',font='bold'):
    return f'guibg={bg} guifg={fg} gui={font}'

def get_color_mode(mode,mode_theme):
        return mode_theme.get(mode,'#000000')

def add_group_color(name_gorup):
    return f'%#{name_gorup}#'
