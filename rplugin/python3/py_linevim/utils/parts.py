#kelas ini menyimpan part dan icon yang di tampilkan
class Parts:
    def __init__(self) -> None:
        self.mode_bg = {
                'Normal':'#000000',
                'Insert':'#000000',
                'Visual':'#000000',
                'VisualLine':'#000000',
                'VisualBlock':'#000000',
                'Command':'#000000',
                'Replace':'#000000',
                'Terminal':'#000000',
                'Select':'#000000',      
                }
        self.icon_file = '󱔘'
        self.icon_branch = ''
        self.file_name = '%t%m'
        self.row_col= '%l:%c'
        self.section_1 = '#000000'
        self.section_2 = '#000000'
        self.section_3= '#000000'
        self.font_weight = 'NONE'
        self.make_coloum = '%='
        self.border_right = ''
        self.border_left = ''
        self.separator = '•'
        self.icon_mode ='󰭕'
        self.default_border_bg ='#FF000000'

