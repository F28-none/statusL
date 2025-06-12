def render(nvim,statusline,highlight):
    nvim.command(f'set statusline={statusline}')
    for group,color in highlight.items():
       nvim.command(f'highlight {group} {color}')

