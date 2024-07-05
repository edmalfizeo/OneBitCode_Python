from collections import Counter, namedtuple, deque
from operator import itemgetter

# Count items in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(Counter(fruits))

# Using namedtuple
game = namedtuple('game', ['name', 'genre', 'rating'])
g1 = game('GTA V', 'Action', 9.5)
g2 = game('FIFA 24', 'Sports', 8.5)
print(f'\n{g1}')

# Ordering Dictionary
students = {'John': 90, 'Alice': 85, 'Bob': 95}
print(f'\n{sorted(students.items(), key=itemgetter(0))}')

# Using both sides Queue
deq = deque([10, 20, 30, 40, 50])
deq.appendleft(5)
deq.append(60)
print(f'\n{deq}')
deq.popleft()
deq.pop()
print(f'\n{deq}')
