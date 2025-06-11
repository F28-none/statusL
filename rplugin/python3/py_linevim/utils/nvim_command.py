def render(nvim,statusline,mode_color,file_color):
    nvim.command(f'set statusline={statusline}')
    nvim.command(f'highlight mode {mode_color}')
    nvim.command(f'highlight file {file_color}')
