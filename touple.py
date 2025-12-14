#A tuple is a collection of items in Python that is 
# ordered,Immutable (cannot be changed),Allows duplicate values
my_tuple = (10, 20, 30)
#Creating Tuples
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (10, "hello", True)
t4= (5,)   # comma is necessary for single item in tuple 
#Accessing Tuple Elements (Indexing)
t = (10, 20, 30, 40)
print(t[0])   # 10
print(t[-1])  # 40

#Tuple Slicing
print(t[1:4])   # (20, 30, 40)

#Tuple is Immutable ❌
t[1] = 100

#if you to do comvert it into list 
t = list(t)
t[1] = 100
t = tuple(t)

#Tuple Operations::::::::::::::::::::
#concatentation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)
#repetition
t = (1, 2)
print(t * 3)
# Membership Operator
print(20 in t)  
print(50 not in t)

#Length Operator
print(len(t))
'''
| Function  | Use           |
| --------- | ------------- |
| `len()`   | Length        |
| `max()`   | Maximum value |
| `min()`   | Minimum value |
| `sum()`   | Sum           |
| `count()` | Count value   |
| `index()` | Find index    |

'''

#Looping Through Tuples
for item in t2:
    print(item)