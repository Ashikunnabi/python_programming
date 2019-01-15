i_am_global = 5

def functions():
    i_am_local = 6
    hi_i_am_local_too = 60
    
    print('Global:', i_am_global)
    print('Local:', i_am_local)
    print('\nGlobal Keys:\n', globals().keys())
    print('\nLocal Keys:\n', locals().keys())

foo = 1
def foos():
    foo = 5
    print('\nGlobal:', globals()['foo'])
    print('Local:', locals()['foo'])
    
functions()
foos()
