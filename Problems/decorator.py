def dec_func(func):
    def wrap_func():
        print('abc')
        return func()
    print('dec_func worked')
    return wrap_func

# def show():
#     print('show worked')

# dec_show = dec_func(show)
# dec_show()

@dec_func
def display():
    print('In display')

display()