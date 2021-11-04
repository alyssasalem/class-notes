""" notes for memory class"""

a = ['1', '2', '3']    # assign a's value, assign a path
b = a                  # b points to a's path (same path)
print(id(a))           # check ids
print(id(b))           # - - -
print(a)               # check values (same values)
print(b)               # - - -
print(a is b)          # a is b? yus

a.append('4')          # change value at end of a's path
print(id(a))           # print ids (stay the same, point at same target)
print(id(b))           # - - -
print(a)               # check values (both have changed)
print(b)               # - - -
print(a is b)          # a is b? yus

a = a + ['4']          # change a's target
print(id(a))           # Print ids (a's path has changed)
print(id(b))           # - - -
print(a)               # check values (a's value has changed)
print(b)               # - - -
print(a is b)          # a is b? nah
