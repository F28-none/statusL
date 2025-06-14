from pynvim import plugin,autocmd,function
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

    @function('Py_line_config',sync=True)
    def user_config(self,args):
        try:
            if not args or not isinstance(args[0], dict):
                raise ValueError('Konfigurasi harus dictionary')
            data = args[0]
            #only user can config
            mode_data = data.get('mode_bg',{})
            key_user = mode_data.keys()
            key_base = self.parts.mode_bg.keys()
            for key in key_user:
                if not key in key_base:
                    raise ValueError(f'maaf mode {key} bukan mode nvim') 
            self.parts.mode_bg = mode_data
            self.parts.section_2= data.get('file_bg',self.parts.section_2)
            self.parts.section_3= data.get('branch_bg',self.parts.section_3)
            self.parts.pipe= data.get('pipe',self.parts.pipe)
            self.parts.icon_file= data.get('icon_file',self.parts.icon_file)
            self.parts.icon_branch= data.get('icon_branch',self.parts.icon_branch)
            self.parts.shape_left= data.get('separator_left',self.parts.shape_left)
            self.parts.shape_right= data.get('separator_right',self.parts.shape_right)
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
        branch_name = get_branch_name()
        info_branch = get_branch_info()

        if not branch_name:
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

        """
        di sini saya memggunakan \\ untuk menghendel
        agar memastikan penghubung tiap section adalah string
        bukan caracter seperti |
        """
        style_status = {
            'pipe2':{
                'pipe2':f'\\{self.parts.pipe}',
            },
            'shape_left1':{
                'shape_group':'%#shapeMode#',
                'shape':self.parts.shape_left,
            },
            'nv_icon':{
                'mode_group':'%#mode#',
                'icon':self.parts.icon_mode,
            },
            'mode':{
                'mode_group':'%#mode#',
                'mode_part':mode,
            },
            'shape_left2':{
                'shape_group':'%#shapeMode#',
                'shape':self.parts.shape_right,
            },
            'pipe3':{
                'pipe_group':'%#pipe#',
                'pipe3':f'\\{self.parts.pipe}',
            },
            'shape_left3':{
                'shape_group':'%#shapeFile#',
                'shape':self.parts.shape_left,
            },
            'file':{
                'file_group':'%#file#',
                'file_icon':self.parts.icon_file,
                'file_part':self.parts.filename,
            },
            'shape_left4':{
                'shape_group':'%#shapeFile#',
                'shape':self.parts.shape_right,
            },
            'pipe4':{
                'pipe_group':'%#pipe#',
                'pipe1':f'\\{self.parts.pipe}',
            },
            'shape_left6':{
                'shape_group':'%#shapeBranch#',
                'shape':self.parts.shape_left,
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
            'shape_left5':{
                'shape_group':'%#shapeBranch#',
                'shape':self.parts.shape_right,
            },
            'pipe1':{
                'pipe_group':'%#pipe#',
                'pipe1':f'\\{self.parts.pipe}',
            },
        }
        render(self.nvim,style_status,highlight)
