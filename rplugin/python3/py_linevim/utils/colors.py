def send_color(bg='#000000',fg='#ffffff',font='bold'):
    return f'guibg={bg} guifg={fg} gui={font}'

def get_color_mode(mode,mode_theme):
        return mode_theme.get(mode,'#000000')

def highlight_part(self,mode_core):
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
        return highlight
