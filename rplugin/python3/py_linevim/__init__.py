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

    """
    Fungsi ini di gunakan untuk menagani Konfigurasi dari user
    """
    @function('Py_line_config',sync=True)
    def user_config(self,args):
        """
        Pengecheckan untuk memvalidasi Konfigurasi Harus sebuah dict
        """
        try:
            if not args or not isinstance(args[0], dict):
                raise ValueError('Konfigurasi harus dictionary')
            config = args[0]
            #only user can config
            config_mode = config.get('mode_bg',{})
            key_user = config_mode.keys()
            """
            Melakukan Pengecheckan ,key yang di kirim harus valid dengan key dari base
            """
            key_base = self.parts.mode_bg.keys()
            for key in key_user:
                if not key in key_base:
                    raise ValueError(f'maaf mode {key} bukan mode nvim') 

            self.parts.mode_bg =config_mode 
            self.parts.section_2= config.get('file_bg',self.parts.section_2)
            self.parts.section_3= config.get('branch_bg',self.parts.section_3)
            self.parts.separator= config.get('separator',self.parts.separator)
            self.parts.icon_file= config.get('icon_file',self.parts.icon_file)
            self.parts.icon_branch= config.get('icon_branch',self.parts.icon_branch)
            self.parts.border_left= config.get('border_left',self.parts.border_left)
            self.parts.border_right= config.get('border_right',self.parts.border_right)
            self.parts.icon_mode= config.get('icon_mode',self.parts.icon_mode)
        except Exception as e:
            self.nvim.command(f'echo"[PyLine Error] Config gagal: {e}\n"')
        
    """
    jalankan pertamakali neovim di buka
    """
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
    @autocmd('ModeChanged,BufWritePost',pattern='*',sync=True)
    def set_status_line(self):
        mode_core = self.get_mode_nvim()
        """
        mode core yg di dapatkan dari neovim,
        hanya karakter n,i,v dll.
        di sini saya memfilter agar mode lebih informatif,
        contoh : n >> Normal
        """
        mode = info_mode(mode_core)

        branch_name = get_branch_name()
        info_branch = get_branch_info()

        """
        Jika directori saat nvim di buka,
        bukan .git atau git repo akan di gantikan dengan syimbol di bawah
        """
        if not branch_name:
            branch_name = ''

        #separator color for integrated with mode
        #section 1
        """
        sepesial border untuk section mode,
        agar border selalu mengitu warna bg dan fg dari mode
        """
        mode_color = send_color(get_color_mode(mode_core,self.parts.mode_bg))
        border_color_mode = send_color(self.parts.default_border_bg,get_color_mode(mode_core,self.parts.mode_bg))

        #section 2 
        file_color = send_color(self.parts.section_2)
        border_color_file = send_color(self.parts.default_border_bg,self.parts.section_2)

        #section 3
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

        """
        di sini saya memggunakan \\ untuk menghendel
        agar memastikan penghubung tiap section adalah string
        bukan caracter seperti |
        """
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
