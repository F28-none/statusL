#membangun semua komponen dan part menjadi 1
def build(parts):
    status = []
    for key,valtype in parts.items():
        for part,value in valtype.items():
            status.append(value)
            
    return ''.join(status)


