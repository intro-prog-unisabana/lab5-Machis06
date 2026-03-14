def set_globals(some_int, some_str):
    global global_int
    global global_str
    
    global_int = some_int
    global_str = some_str

def get_globals():
    return (globals().get("global_int"), globals().get("global_str"))
