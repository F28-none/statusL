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

    @autocmd('VimEnter',sync=True)
    def on_open(self):
        self.set_status_line()

    def get_mode_nvim(self):
        return self.nvim.funcs.mode()
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
        shape = self.parts.shape

        if not branch_name:
            icon_branch = ''
            branch_name = ''
        #group color
        group_color = {
            'mode':'%#mode#',
            'file':'%#file#',
            'shape':'%#shape#',

        }

        mode_color = send_color(get_color_mode(mode_core))
        file_color = send_color()
        shape_color = send_color('#000000',get_color_mode(mode_core))

        higlight = {
            'mode':mode_color,
            'file':file_color,
            'shape':shape_color,
        }

        statusline = build(
            group_color['mode'],
            mode,
            group_color['shape'],
            shape,
            group_color['file'],
            icon_file,
            file_name,
            make_coloum,
            icon_branch,
            branch_name,
            info_branch,
            group_color['mode'],
            row_col,
            group_color['shape'],
            shape,
        )
        render(self.nvim,statusline,higlight)
