# Enter your code here
my_tuple = (0, 1, 2, "hi", 4, 5)

my_tuple = my_tuple[0:3] + (3,) + my_tuple[4:]
print(my_tuple)