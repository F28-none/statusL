#menerapkan semua yg komponen ke statusline neovim
def render(nvim,parts,highlight):
    #build status 
    try:
        status = []
        for key,valtype in parts.items():
            for part,value in valtype.items():
                status.append(value)
        statusline = ''.join(status)
    #highlight status
        nvim.command(f'set statusline={statusline}')
        for group,color in highlight.items():
           nvim.command(f'highlight {group} {color}')
    except Exception as e:
        nvim.command(f'eror saat build status {e}')


