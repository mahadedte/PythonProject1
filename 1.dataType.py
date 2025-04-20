# boolean data type
x = 10
y = 20
print(x > y)
# False
print(y > x)
# True


# list data type
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lst)
print(type(lst))
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# <class 'list'>


# tuple data type
tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(tpl)
print(type(tpl))
# (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# <class 'tuple'>

# set data type
st = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
print(st)
print(type(st))
# {100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
# <class 'set'>

# string data type
st = 'python'
print(st)
print(type(st))
# python
# <class 'str'>

# range data type
rng = range(10)
print(rng)
print(list(rng))
# range(0, 10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(10) creates a range object from 0 to 9.
# Printing it directly shows range(0, 10); use list(range(10)) to see the numbers.

# dictionary
dct = {'name': 'mahade', 'email': 'wtbl.hasan@gmail.com', 'contact': '01771752777'}
print(dct)
# {'name': 'mahade', 'email': 'wtbl.hasan@gmail.com', 'contact': '01771752777'}
print(type(dct))
# <class 'dict'>
print(dct.keys())
# dict_keys(['name', 'email', 'contact'])
print(dct.values())
# dict_values(['mahade', 'wtbl.hasan@gmail.com', '01771752777'])
