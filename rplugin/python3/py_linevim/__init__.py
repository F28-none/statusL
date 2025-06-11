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
        mode = info_mode(self.get_mode_nvim())
        icon_file = self.parts.icon_file
        file_name = self.parts.filename
        separator = self.parts.separator
        icon_branch = self.parts.icon_branch
        branch_name = get_branch_name()
        info_branch = get_branch_info()
        row_col = self.parts.row_col

        if not branch_name:
            icon_branch = ''
            branch_name = ''
        #group color
        mode_group = '%#mode#'
        file_group = '%#file#'

        mode_color = send_color(get_color_mode(self.get_mode_nvim()))
        file_color = send_color()
        statusline = build(
            mode_group,
            mode,
            file_group,
            icon_file,
            file_name,
            separator,
            icon_branch,
            branch_name,
            info_branch,
            row_col,
        )
        render(self.nvim,statusline,mode_color,file_color)
