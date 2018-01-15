
global_var = 20

def out_func():
    out = 10
    # nonlocal global_var
    global global_var
    global_var = global_var + 2
    def in_func():
        # global out # 这里不能这么用，需要按照下面走
        nonlocal out
        out = out + 2
        print(out)
    
    in_func()

out_func()
