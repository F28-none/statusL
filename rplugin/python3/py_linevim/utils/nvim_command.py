def apply_statusline(nvim,statusline,highlight):
    try:
        nvim.command(f'set statusline={statusline}')
        for group,color in highlight.items():
           nvim.command(f'highlight {group} {color}')
    except Exception as e:
        nvim.command(f'eror saat build status {e}')


