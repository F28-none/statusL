#membuat info menjadi kebih informatif
def info_mode(mode):
    match mode:
        case 'n': return 'Normal'
        case 'i': return 'Insert'
        case 'v': return 'Visual'
        case 'V': return 'Visual\\ Line'
        case "\x16": return 'Visual\\ Block'
        case 'c': return 'Command'
        case 'R': return 'Replace'
        case 't': return 'Terminal'
        case 's': return 'Select'

