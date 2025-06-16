from pynvim import plugin,autocmd,function
from py_linevim.utils.user_config_handle import handle
from py_linevim.utils.mode import info_mode
from py_linevim.utils.parts import Parts 
from py_linevim.utils.git import get_branch_info,get_branch_name
from py_linevim.utils.colors import send_color,get_color_mode
from py_linevim.utils.nvim_command import render 

@plugin
class PyLine:
    def __init__(self,nvim) -> None:
        self.nvim = nvim
        self.parts = Parts()

    @autocmd('VimEnter',sync=True)
    def on_open(self):
        try:
            self.set_status_line()
        except Exception as e:
            self.nvim.command(f'echo "Plugin eror{e}"')

    def get_mode_nvim(self):
        return self.nvim.funcs.mode()

    @function('Py_line_config',sync=True)
    def user_config(self,args):
        handle(self,args)
    #mengambil info mode dari neovim

    #CORE
    @autocmd('ModeChanged,BufWritePost',pattern='*',sync=True)
    def set_status_line(self):
        #feature
        mode = info_mode(self.get_mode_nvim())
        branch_name = get_branch_name()
        info_branch = get_branch_info()

        mode_color = send_color(get_color_mode(mode,self.parts.mode_bg))
        border_color_mode = send_color(self.parts.default_border_bg,get_color_mode(mode,self.parts.mode_bg))
        file_color = send_color(self.parts.section_2)
        border_color_file = send_color(self.parts.default_border_bg,self.parts.section_2)
        border_color_branch = send_color(self.parts.default_border_bg,self.parts.section_3)
        branch_color = send_color(self.parts.section_3)
        highlight = {
            'branch':branch_color,
            'mode':mode_color,
            'borderMode':border_color_mode, #sepesial group untuk border mode
            'borderBranch':border_color_branch,
            'borderFile':border_color_file,
            'file':file_color,
        }
        style_status = {
            'separator2':{
                'separator2':f'\\{self.parts.separator}',
            },
            'border_left1':{
                'border_group':'%#borderMode#',
                'border':self.parts.border_left,
            },
            'nv_icon':{
                'mode_group':'%#mode#',
                'icon':self.parts.icon_mode,
            },
            'mode':{
                'mode_group':'%#mode#',
                'mode_part':mode,
            },
            'border_left2':{
                'border_group':'%#borderMode#',
                'border':self.parts.border_right,
            },
            'separator3':{
                'separator_group':'%#separator#',
                'separator3':f'\\{self.parts.separator}',
            },
            'border_left3':{
                'border_group':'%#borderFile#',
                'border':self.parts.border_left,
            },
            'file':{
                'file_group':'%#file#',
                'file_icon':self.parts.icon_file,
                'file_part':self.parts.file_name,
            },
            'border_left4':{
                'border_group':'%#borderFile#',
                'border':self.parts.border_right,
            },
            'separator4':{
                'separator_group':'%#separator#',
                'separator1':f'\\{self.parts.separator}',
            },
            'border_left6':{
                'border_group':'%#borderBranch#',
                'border':self.parts.border_left,
            },
            'branch':{
                'branch_group':'%#branch#',
                'branch_icon':self.parts.icon_branch,
                'branch_part':branch_name,
                'branch_status':info_branch,
            },
            'colom':{
                'branch_group':'%#branch#',
                'colom_part':self.parts.make_coloum,
            },
            'row_col':{
                'row_col_part':self.parts.row_col,
            },
            'border_left5':{
                'border_group':'%#borderBranch#',
                'border':self.parts.border_right,
            },
            'separator1':{
                'separator_group':'%#separator#',
                'separator1':f'\\{self.parts.separator}',
            },
        }
        render(self.nvim,style_status,highlight)
