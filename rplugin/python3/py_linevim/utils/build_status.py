def statusline_build(parts,mode,branch_name,info_branch):
        style_status = {
            'separator2':{
                'separator2':f'\\{parts.separator}',
            },
            'border_left1':{
                'border_group':'%#borderMode#',
                'border':parts.border_left,
            },
            'nv_icon':{
                'mode_group':'%#mode#',
                'icon':parts.icon_mode,
            },
            'mode':{
                'mode_group':'%#mode#',
                'mode_part':mode,
            },
            'border_left2':{
                'border_group':'%#borderMode#',
                'border':parts.border_right,
            },
            'separator3':{
                'separator_group':'%#separator#',
                'separator3':f'\\{parts.separator}',
            },
            'border_left3':{
                'border_group':'%#borderFile#',
                'border':parts.border_left,
            },
            'file':{
                'file_group':'%#file#',
                'file_icon':parts.icon_file,
                'file_part':parts.file_name,
            },
            'border_left4':{
                'border_group':'%#borderFile#',
                'border':parts.border_right,
            },
            'separator4':{
                'separator_group':'%#separator#',
                'separator1':f'\\{parts.separator}',
            },
            'border_left6':{
                'border_group':'%#borderBranch#',
                'border':parts.border_left,
            },
            'branch':{
                'branch_group':'%#branch#',
                'branch_icon':parts.icon_branch,
                'branch_part':branch_name,
                'branch_status':info_branch,
            },
            'colom':{
                'branch_group':'%#branch#',
                'colom_part':parts.make_coloum,
            },
            'row_col':{
                'row_col_part':parts.row_col,
            },
            'border_left5':{
                'border_group':'%#borderBranch#',
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
