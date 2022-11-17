from itertools2 import count
for i in count(10):
    print(i)
    if i == 15:
        break
    
from itertools2 import cycle
a = [1,2,3,4]
for i in cycle(a):
    print(i)
    if i == 3:
        break
    
from itertools2 import repeat
a = [1,2,3,4]
for i in repeat(3):
    print(i)
