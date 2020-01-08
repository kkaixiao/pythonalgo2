
def my_func(x, y, z):
    print(x,y,z)


list_vect = [2, 3, -1]
tuple_vec = (2, 3, -1)
dict_vect = {'x': 2, 'y': 3, 'z': -1}


my_func(*list_vect)
my_func(*tuple_vec)
my_func(**dict_vect)
