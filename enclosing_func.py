# scopes3.py
# Local, Enclosing and Global

def enclosing_func():
    m = 13

    def local():
        m = 4
        # m doesn't belong to the scope defined by the local
        # function so Python will keep looking into the next
        # enclosing scope. This time m is found in the enclosing
        # scope
        print(m, 'printing from the local scope')

    # calling the function local
    local()
    print(m, 'printing from the local scope')

m = 5
print(m, 'printing from the global scope')

enclosing_func()