#mendefiniikan dan membuat configurasi color
def send_color(bg='#000000',fg='#ffffff',font='bold'):
    return f'guibg={bg} guifg={fg} gui={font}'

#mngubah warna di setiao masing masing mode
def get_color_mode(mode):
        bg_color = '#6f03fc'  # default
        match mode:
            case 'i': return '#44bcd8'
            case 'v': return '#1979a9'
            case 'n': return '#69bdd2'
            case 'V': return '#b8182b'
            case "\\x16": return '#b9292o'
            case 'c': return '#99baa8'
            case 'R': return '#99baa8'
            case 't': return '#99baa8'
            case 's': return '#99baa8'
        return bg_color
