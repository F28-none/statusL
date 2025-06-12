from pynvim import plugin,autocmd
from py_linevim.utils.mode import info_mode
from py_linevim.utils.parts import Parts 
from py_linevim.utils.git import get_branch_info,get_branch_name
from py_linevim.utils.build_statusline import build
from py_linevim.utils.colors import send_color,get_color_mode
from py_linevim.utils.nvim_command import render 

@plugin
class PyLine:
    def __init__(self,nvim) -> None:
        self.nvim = nvim
        self.parts = Parts()

    #set pertama kali saat di membuka neovim
    @autocmd('VimEnter',sync=True)
    def on_open(self):
        self.set_status_line()

    #mengambil info mode dari neovim
    def get_mode_nvim(self):
        return self.nvim.funcs.mode()

    #CORE
    @autocmd('ModeChanged',sync=True)
    def set_status_line(self):
        mode_core = self.get_mode_nvim()
        mode = info_mode(mode_core)
        icon_file = self.parts.icon_file
        file_name = self.parts.filename
        make_coloum = self.parts.make_coloum
        icon_branch = self.parts.icon_branch
        branch_name = get_branch_name()
        info_branch = get_branch_info()
        row_col = self.parts.row_col
        shape_left = self.parts.shape_left
        shape_right = self.parts.shape_right
        circle_icon = self.parts.circle_dec


        if not branch_name:
            icon_branch = ''
            branch_name = ''

        mode_color = send_color(get_color_mode(mode_core))
        file_color = send_color('#9c8f32')
        shape_color = send_color('#FF000000','#9c8f32')
        shape_color_mode = send_color('#FF000000',get_color_mode(mode_core))

        highlight = {
            'mode':mode_color,
            'shapeMode':shape_color_mode,
            'shape':shape_color,
            'file':file_color,
        }

        style_status = {
            'pipe2':{
                'pipe2':circle_icon,
            },
            'shape_left_mode':{
                'mode_group':'%#shapeMode#',
                'shape_icon':shape_left,
            },
            'mode':{
                'mode_group':'%#mode#',
                'mode_part':mode,
            },
            'shape_right_mode':{
                'mode_group':'%#shapeMode#',
                'shape_icon':shape_right,
            },
            'pipe3':{
                'pipe3':circle_icon,
            },
            'shape_left_file':{
                'mode_group':'%#shape#',
                'shape_icon':shape_left,
            },
            'file':{
                'file_group':'%#file#',
                'file_icon':icon_file,
                'file_part':file_name,
            },
            'colom':{
                'colom_part':make_coloum,
            },
            'branch':{
                'branch_icon':icon_branch,
                'branch_part':branch_name,
                'branch_status':info_branch,
            },
            'row_col':{
                'row_col_part':row_col,
            },
            'shape_end_status':{
                'mode_group':'%#shape#',
                'shape_icon':shape_right,
            },
            'pipe1':{
                'pipe1':circle_icon,
            },
        }

        statusline = build(style_status)

        render(self.nvim,statusline,highlight)
