from pynvim import plugin,autocmd,function

from py_linevim.utils.parts import Parts 
from py_linevim.utils.mode import info_mode
from py_linevim.utils.git import get_branch_info,get_branch_name

from py_linevim.utils.colors import apply_color,get_color_mode,add_group_color
from py_linevim.utils.build_status import statusline_build
from py_linevim.utils.nvim_command import apply_statusline 
from py_linevim.utils.user_config import edit_parts

@plugin
class PyLine:
    def __init__(self,nvim) -> None:
        self.nvim = nvim
        self.parts = Parts()

    @function('Py_line_config',sync=True)
    def user_config(self,args):
        edit_parts(self,args)

    @autocmd('VimEnter',sync=True)
    def on_open(self):
        try:
            self.set_status_line()
        except Exception as e:
            self.nvim.command(f'echo "Plugin eror{e}"')

    def get_mode_nvim(self):
        return self.nvim.funcs.mode()

    @autocmd('ModeChanged,BufWritePost',pattern='*',sync=True)
    def set_status_line(self):
        mode = info_mode(self.get_mode_nvim())
        branch_name = get_branch_name()
        info_branch = get_branch_info()

        highlight = {
            'branch':apply_color(self.parts.section_3),
            'mode':apply_color(get_color_mode(mode,self.parts.mode_bg)),
            'borderMode':apply_color(self.parts.default_border_bg,get_color_mode(mode,self.parts.mode_bg)), #sepesial group untuk border mode
            'borderBranch':apply_color(self.parts.default_border_bg,self.parts.section_3),
            'borderFile':apply_color(self.parts.default_border_bg,self.parts.section_2),
            'file':apply_color(self.parts.section_2),
        }

        statusline = statusline_build(self.parts,mode,branch_name,info_branch)
        apply_statusline(self.nvim,statusline,highlight)
