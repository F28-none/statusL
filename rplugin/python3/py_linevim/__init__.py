from pynvim import plugin,autocmd,function
from py_linevim.utils.user_config_handle import handle
from py_linevim.utils.mode import info_mode
from py_linevim.utils.parts import Parts 
from py_linevim.utils.git import get_branch_info,get_branch_name
from py_linevim.utils.colors import highlight_part
from py_linevim.utils.nvim_command import render 

@plugin
class PyLine:
    def __init__(self,nvim) -> None:
        self.nvim = nvim
        self.parts = Parts()

    def get_mode_nvim(self):
        return self.nvim.funcs.mode()


    @autocmd('VimEnter',sync=True)
    def on_open(self):
        try:
            self.set_status_line()
        except Exception as e:
            self.nvim.command(f'echo "Plugin eror{e}"')

    @function('Py_line_config',sync=True)
    def user_config(self,args):
        handle(self,args)


    #mengambil info mode dari neovim
    #CORE
    @autocmd('ModeChanged,BufWritePost',pattern='*',sync=True)
    def set_status_line(self):
        mode_core = self.get_mode_nvim()
        mode = info_mode(mode_core)
        branch_name = get_branch_name()
        info_branch = get_branch_info()

        if not branch_name:
            branch_name = ''

        highlight = highlight_part(self,mode_core) 

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
