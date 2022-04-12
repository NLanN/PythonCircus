
# Declaring a dictionary
d = {} 
  
# This is the list which we are 
# trying to use as a key to
# the dictionary
a =(1, 2, 3, 4, 5)
  
# converting the list a to a string

d[a]= 1
  
# converting the list a to a tuple
print(d)

b = ('a',1)

print(b)

print(b.__hash__())