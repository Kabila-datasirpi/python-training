#function without parameters
def myfun():
    print("good morning")
myfun()

#function with parameters
def addtion(a,b):
    c=a+b
    return c
print(addtion(1,2))

#args
def fun(*args):
    d=sum(args)
    return d
print(fun(4,5,6,9))

#lamda function
multiply=lambda d,c:d*c
print(multiply(4,3))
