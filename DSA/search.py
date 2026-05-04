l = [ 100, 2, 4, 9, 10] # <-- List

def search(x):
    print(type(x))
    for _ in l:
        if _ == x:
            print('found')
            return
    print('not found')

search('10')

