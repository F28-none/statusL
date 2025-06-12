def build(args):
    part = []
    for test,val in args.items():
        for gc,cl in val.items():
            part.append(test)
            part.append(gc)
            part.append(cl)
            print(''.join(part))
style_status = {
    'mode':{
        '%#mode#':'color'
    },
}
build(style_status)
