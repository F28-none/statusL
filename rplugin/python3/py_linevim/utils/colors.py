#mendefiniikan dan membuat configurasi color
def send_color(bg='#535e70',fg='#ffffff'):
    return f'guibg={bg} guifg={fg}'

#mngubah warna di setiao masing masing mode
def get_color_mode(mode):
        bg_color = '#8c3eb3'  # default
        match mode:
            case 'i': return '#d496f2'
            case 'v': return '#ed4c5f'
            case 'n': return '#8c3eb3'
            case 'V': return '#b8182b'
            case "\\x16": return '#b9292o'
            case 'c': return '#99baa8'
            case 'R': return '#99baa8'
            case 't': return '#99baa8'
            case 's': return '#99baa8'
        return bg_color
