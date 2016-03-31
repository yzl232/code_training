>>> # define a list
>>> my_list = [4, 7, 0, 3]

>>> # get an iterator using iter() on that list
>>> my_iter = iter(my_list)
>>> my_iter
<list_iterator object at 0x00000000031AD9B0>

>>> # iterate through it using next() 
>>> next(my_iter)
4
>>> next(my_iter)
7
