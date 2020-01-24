def mean(*args):
    return sum(args) / len(args)

def foo(*args):
    new_list = [i.upper() for i in args]
    new_list.sort()
    return new_list

print((mean(1,3,4)))

print(foo('sup', 'how', 'are', 'damn'))