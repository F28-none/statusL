"""
file ini mengatur semua highlight atau color,
menggunakan default color jika tidak ada yg di kirim
"""
def send_color(bg='#000000',fg='#ffffff',font='bold'):
    return f'guibg={bg} guifg={fg} gui={font}'

"""
sepesial untuk mengubah color setiap mode
"""
def get_color_mode(mode,mode_theme):
        return mode_theme.get(mode,'#000000')
