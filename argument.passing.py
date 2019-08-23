def func(x):
    print(x)

def func2(x):
    x = 7
    print(x)


x = 3

func(x)
func2(x)

print(x)

y = [1, 2, 3]
def func(x):
    y[1] = 42  # this affects the caller!
    # y = [4,5,6]

func(y)
print(y)  # prints: [1, 42, 3]

def func(a, b, c):
    print(a, b, c)
func(1, 2, 3)  # prints: 1 2 3

func(a=4, c=5, b=6)  # prints: 1 3 2

def func2(a, b=4, c=88):
    print(a, b, c)

func2(1)  # prints: 1 4 88
func2(b=5, a=7, c=9)  # prints: 7 5 9
func2(42, c=9)  # prints: 42 4 9
func2(42, 43, 44)  # prints: 42, 43, 44

def minimum(*n):
    # print(type(n))  # n is a tuple
    if n:  # explained after the code
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1, 3, -7, 9)  # n = (1, 3, -7, 9) - prints: -7
minimum()             # n = () - prints: nothing

def func3(**kwargs):
    print(kwargs)

# All calls equivalent. They print: {'a': 1, 'b': 42}
func3(a=1, b=42)
func3(**{'a': 1, 'b': 42})
func3(**dict(a=1, b=42))

# arguments.variable.db.py
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    # we then connect to the db (commented out)
    # db.connect(**conn_params)

connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')

# arguments.keyword.only.py
def kwo(*a, c):
    print(a, c)

kwo(1, 2, 3, c=7)  # prints: (1, 2, 3) 7
kwo(c=4)  # prints: () 4
# kwo(1, 2)  # breaks, invalid syntax, with the following error
# TypeError: kwo() missing 1 required keyword-only argument: 'c'

def kwo2(a, b=42, *, c):
    print(a, b, c)

kwo2(3, b=7, c=99)  # prints: 3 7 99
kwo2(3, c=13)  # prints: 3 42 13
# kwo2(3, 23)  # breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'

def mutable(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))  # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one

mutable()
mutable()
mutable()