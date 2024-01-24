                                    #variables
x=10
print(x)

y="Kabila"
print(y)

#to get the datatype of the variable
z=type(y)
print(z)

#one value to multiple variables
a=b=c="orange"
print(a)
print(b)
print(c)

#many values to multiple variable in a single line
t=s=j="apple","banana","grapes"
print(t,s,j)

#unpacking a list
cars=["volvo","bmw","audi"]
h,u,i=cars
print(h)
print(u)
print(i)

#global variables
m="happy new year"
def wish():
    global m
    m="happy pongal"
wish()
print(m)
                                #strings

print("hello")

#looping a string
n="janani"
for i in n:
    print(i)

#find the lenth of the string
print(len(n))

#check string
para="Good things happen for a reason"
print("for" in para)

#not in
print("for" not in para)

#slicing a string
txt="good morning"
print(txt[2:5])

#slice from starting
print(txt[:5])

#slice to end
print(txt[1:])

#negative indexing
print(txt[-5:-2])

#concatinate string
t1="wel"
t2="come"
print(t1+t2)

#format strings
q1=35
q2="I want {} bottles"
print(q2.format(q1))


