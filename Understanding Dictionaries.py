# Different ways to update Dictionaries

#####################################

d = {'x': 2}

d.update(x = 3)
print(d)

#####################################

a = {1: "one", 2: "three", 3: "three"}
a1 = {2: "two"}

# updates the value of key 2
a.update(a1)
print(a)
