#kelas ini menyimpan part dan icon yang di tampilkan
class Parts:
    def __init__(self) -> None:
        self.mode_bg = {
                'Normal':'#6f03fc',
                'Insert':'#000000',
                'Visual':'#888888',
                'VisualLine':'#888888',
                'VisualBlock':'#888888',
                'Command':'#000000',
                'Replace':'#888888',
                'Terminal':'#888888',
                'Select':'#888888',      
                }
        self.icon_file = '󱔘'
        self.icon_branch = ''
        self.file_name = '%t%m'
        self.row_col= '%l:%c'
        self.section_1 = '#6f03fc'
        self.section_2 = '#6f03fc'
        self.section_3= '#6f03fc'
        self.font_weight = 'NONE'
        self.make_coloum = '%='
        self.border_right = ''
        self.border_left = ''
        self.separator = '•'
        self.icon_mode ='󰭕'
        self.default_border_bg ='#FF000000'

