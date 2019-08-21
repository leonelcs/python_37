from collections import namedtuple
from collections import defaultdict

Vision = namedtuple('Vision', ['left','right'])

vision = Vision(9.5, 8.8)

print("left", vision.left)
print("right", vision.right)

dd = defaultdict(int)

dd['age'] += 1

print(dd)