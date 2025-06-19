def statusline_build(parts,mode,branch_name,info_branch,group):
        style_status = {
            'separator2':{
                'separator2':f'\\{parts.separator}',
            },
            'border_left1':{
                'border_mode_group':group.get('border_mode_group'),
                'border':parts.border_left,
            },
            'nv_icon':{
                'mode_group':group.get('mode_group'),
                'icon':parts.icon_mode,
            },
            'mode':{
                'mode_group':group.get('mode_group'),
                'mode_part':mode,
            },
            'border_left2':{
                'border_mode_group':group.get('border_mode_group'),
                'border':parts.border_right,
            },
            'separator3':{
                'separator_group':'%#separator#',
                'separator3':f'\\{parts.separator}',
            },
            'border_left3':{
                'border_file':group.get('border_file'),
                'border':parts.border_left,
            },
            'file':{
                'file_group':group.get('file_group'),
                'file_icon':parts.icon_file,
                'file_part':parts.file_name,
            },
            'border_left4':{
                'border_file':group.get('border_file'),
                'border':parts.border_right,
            },
            'separator4':{
                'separator_group':'%#separator#',
                'separator1':f'\\{parts.separator}',
            },
            'border_left6':{
                'border_branch':group.get('border_branch'),
                'border':parts.border_left,
            },
            'branch':{
                'branch_group':group.get('branch_group'),
                'branch_icon':parts.icon_branch,
                'branch_part':branch_name,
                'branch_status':info_branch,
            },
            'colom':{
                'branch_group':group.get('branch_group'),
                'colom_part':parts.make_coloum,
            },
            'row_col':{
                'row_col_part':parts.row_col,
            },
            'border_left5':{
                'border_branch':group.get('border_branch'),
                'border':parts.border_right,
            },
            'separator1':{
                'separator_group':'%#separator#',
                'separator1':f'\\{parts.separator}',
            },
        }
        status = []
        for key,valtype in style_status.items():
            for part,value in valtype.items():
                status.append(value)
        statusline = ''.join(status)
        return statusline
