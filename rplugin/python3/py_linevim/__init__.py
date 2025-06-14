from pynvim import plugin,autocmd,function
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

    @function('Py_line_config',sync=True)
    def user_config(self,args):
        try:
            if not args or not isinstance(args[0], dict):
                raise ValueError('Konfigurasi harus dictionary')
            data = args[0]
            mode_data = data.get('mode_bg',{})
            key_user = mode_data.keys()
            key_base = self.parts.mode_bg.keys()
            for key in key_user:
                if not key in key_base:
                    raise Exception 
            self.parts.mode_bg = mode_data
            self.parts.section_2= data.get('file_bg','#000000')
            self.parts.section_3= data.get('branch_bg','#000000')
            self.parts.pipe= data.get('pipe','•')
            self.parts.icon_file= data.get('icon_file','󱔘')
            self.parts.icon_branch= data.get('icon_branch','')
        except Exception as e:
            self.nvim.command(f'echo"[PyLine Error] Config gagal: {e}\n"')
        


    #set pertama kali saat di membuka neovim
    @autocmd('VimEnter',sync=True)
    def on_open(self):
        try:
            self.set_status_line()
        except Exception as e:
            self.nvim.command(f'echo "Plugin eror{e}"')

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
        circle_icon = f'\\{self.parts.pipe}'


        if not branch_name:
            icon_branch = ''
            branch_name = ''

        #separator color for integrated with mode
        #section 1
        mode_color = send_color(get_color_mode(mode_core,self.parts.mode_bg))
        shape_color_mode = send_color('#FF000000',get_color_mode(mode_core,self.parts.mode_bg))

        #section 2 
        file_color = send_color(self.parts.section_2)
        shape_color_file = send_color('#FF000000',self.parts.section_2)

        #section 3
        shape_color_branch = send_color('#FF000000',self.parts.section_3)
        branch_color = send_color(self.parts.section_3)

        highlight = {
            'branch':branch_color,
            'mode':mode_color,
            'shapeMode':shape_color_mode,
            'shapeBranch':shape_color_branch,
            'shapeFile':shape_color_file,
            'file':file_color,
        }

        style_status = {
            'pipe2':{
                'pipe2':circle_icon,
            },
            'shape_left1':{
                'shape_group':'%#shapeMode#',
                'shape':shape_left,
            },
            'nv_icon':{
                'mode_group':'%#mode#',
                'icon':'󰭕',
            },
            'mode':{
                'mode_group':'%#mode#',
                'mode_part':mode,
            },
            'shape_left2':{
                'shape_group':'%#shapeMode#',
                'shape':shape_right,
            },
            'pipe3':{
                'pipe_group':'%#pipe#',
                'pipe3':circle_icon,
            },
            'shape_left3':{
                'shape_group':'%#shapeFile#',
                'shape':shape_left,
            },
            'file':{
                'file_group':'%#file#',
                'file_icon':icon_file,
                'file_part':file_name,
            },
            'shape_left4':{
                'shape_group':'%#shapeFile#',
                'shape':shape_right,
            },
            'pipe4':{
                'pipe_group':'%#pipe#',
                'pipe1':circle_icon,
            },
            'shape_left6':{
                'shape_group':'%#shapeBranch#',
                'shape':shape_left,
            },
            'branch':{
                'branch_group':'%#branch#',
                'branch_icon':icon_branch,
                'branch_part':branch_name,
                'branch_status':info_branch,
            },
            'colom':{
                'branch_group':'%#branch#',
                'colom_part':make_coloum,
            },
            'row_col':{
                'row_col_part':row_col,
            },
            'shape_left5':{
                'shape_group':'%#shapeBranch#',
                'shape':shape_right,
            },
            'pipe1':{
                'pipe_group':'%#pipe#',
                'pipe1':circle_icon,
            },
        }

        statusline = build(style_status)

        render(self.nvim,statusline,highlight)
