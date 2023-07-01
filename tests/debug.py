lst = [1,2,3,4,5]

def get_out(l):
    l.pop(0)


def t(l):
    print(l)
    get_out(l)
    print(l)
    get_out(l)
    print(l)


t(lst)