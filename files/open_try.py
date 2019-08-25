# files/open_try.py
try:
    fh = open('fear.txt', 'rt')
    # for line in fh.readlines():
    for line in fh:
        print(line.strip())
finally:
    fh.close()

with open('fear.txt') as fh:
    for line in fh:
        print(line.strip())

# printing to a file
with open('print_example.txt', 'w') as fw:
    print('Hey I am printing into a file!!!', file=fw)

# Lendo e escrevendo
with open('fear.txt') as f:
    lines = [line.rstrip() for line in f]

with open('fear_copy.txt', 'w') as fw:
    fw.write('\n'.join(lines))