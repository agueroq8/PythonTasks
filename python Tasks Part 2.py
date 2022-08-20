dash = "----------------------------------------------------------------------"

print("Create a simple function that takes 2 numbers and print their values")

def SimpleFunction(x,y):
    result = "First Value : ",x,"Seconed Value : ",y
    return result
print(SimpleFunction(2,3))
   
print(dash)

print("In the above return function , use keyword arguments when calling the function")

def SimpleFunction(x,y):
    result = "First Value : ",x,"Seconed Value : ",y
    return x,y
print(SimpleFunction(2,3))
   
print(dash)

print("In the above return function , give x and y default values of 0 and call the function with no arguments")

def SimpleFunction(x=0,y=0):
    result = "First Value : ",x,"Seconed Value : ",y
    return x,y
print(SimpleFunction())

print(dash)

print("Create a function that can take any number of arguments and print the sum of them ")

def sum_(x,y):
    result = x + y
    return result

print(sum_(5,5))

print(dash)

print("Create the same sum function using the lambda")
lambdasum = lambda x,y : x+y
print(lambdasum(4,4))

print(dash)
print("Call the lambda function at the same definition line")
SameLineLambda = (lambda x,y : x*y)(5,5)
print(SameLineLambda)

print(dash)

print("Write the difference between the local variable and global variable ?")
print('''local variable its calls for variables inside function or class not global all projects , its help in case developer want to track varablies
knows where changes or problems and global uses for const varablies no need to change it all project ''')

print(dash)
