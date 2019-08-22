surnames = ['Rivest', 'Shamir', 'Adleman'] 
for position in range(len(surnames)): 
    print(position, surnames[position]) 

for position, surname in enumerate(surnames): 
    print(position, surname)

for position, surname in enumerate(sorted(surnames)): 
    print(position, surname)

n = 39
remainders = []
while n > 0:
    remainder = n % 2  # remainder of division by 2
    remainders.insert(0, remainder)  # we keep track of remainders
    n //= 2  # we divide n by 2

print(remainders)

people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1