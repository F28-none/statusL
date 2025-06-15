def handle(self,args):
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
