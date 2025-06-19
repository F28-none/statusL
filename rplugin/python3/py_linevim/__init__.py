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

    def get_mode_nvim(self):
        return self.nvim.funcs.mode()

    @function('Py_line_config',sync=True)
    def user_config(self,args):
        edit_parts(self,args)

    @autocmd('VimEnter',sync=True)
    def on_open(self):
        try:
            self.set_status_line()
        except Exception as e:
            self.nvim.command(f'echo "Plugin eror{e}"')

    @autocmd('ModeChanged,BufWritePost',pattern='*',sync=True)
    def set_status_line(self):
        mode = info_mode(self.get_mode_nvim())
        branch_name = get_branch_name()
        info_branch = get_branch_info()
        group_highlight = self.create_group()
        highlight = self.create_highlight(mode,self.parts,group_highlight)
        try:
            statusline = statusline_build(self.parts,mode,branch_name,info_branch,group_highlight)
            apply_statusline(self.nvim,statusline,highlight)
        except Exception as e:
            self.nvim.command(f'build status failed {e}')

    def create_highlight(self,mode,parts,group):
        highlight = {
            group.get('branch_group').strip('#%'):apply_color(parts.section_3),
            group.get('mode_group').strip('#%'):apply_color(get_color_mode(mode,parts.mode_bg)),
            group.get('border_mode_group').strip('#%'):apply_color(parts.default_border_bg,get_color_mode(mode,parts.mode_bg)),
            group.get('border_branch').strip('#%'):apply_color(parts.default_border_bg,parts.section_3),
            group.get('border_file').strip('#%'):apply_color(parts.default_border_bg,parts.section_2),
            group.get('file_group').strip('#%'):apply_color(parts.section_2),
        }
        return highlight

    def create_group(self):
        group_highlight= {
            'mode_group':add_group_color('mode'),
            'branch_group':add_group_color('branch'),
            'file_group':add_group_color('file'),
            'border_mode_group':add_group_color('borderMode'),
            'border_file':add_group_color('borderFile'),
            'border_branch':add_group_color('borderBranch'),
        }
        return group_highlight

