#kelas ini menyimpan part dan icon yang di tampilkan
class Parts:
    def __init__(self) -> None:
        self.mode_bg = {
            'n':'#6f03fc',
            'i':'#000000',
        }
        self.icon_file = '󱔘'
        self.icon_branch = ''
        self.filename = '%t%m'
        self.row_col= '%l:%c'
        self.fg = '#ffffff'
        self.section_1 = '#6f03fc'
        self.section_2 = '#6f03fc'
        self.section_3= '#6f03fc'
        self.font_weight = 'NONE'
        self.make_coloum = '%='
        self.shape_right = ''
        self.shape_left = ''
        self.circle_dec = '='

