## Example 1 - Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()




## Example 2 - If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)





## Example 3 - Also, use the global keyword if you want to change a global variable inside a function.

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)
