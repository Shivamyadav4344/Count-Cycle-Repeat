from itertools import count
for i in count(10):
    print(i)
    if i == 15:
        break
    
from itertools import cycle
a = [1,2,3,4]
for i in cycle(a):
    print(i)
    if i == 3:
        break
    
from itertools import repeat
a = [1,2,3,4]
for i in repeat(3):
    print(i)