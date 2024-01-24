#if elif else
a=5
b=5
if a>b:
    print("a is Greater")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater")

#short hand if-else
x=15
y=30
print("y is greater") if y>x else print("x is greater")

#Nested if
r=100
if r>50:
    print("r is greater than fifty")
    if r>70:
        print("r is greater than seventy")
    else:
        print("r is not greater than seventy")
else:
    print("r is not greater than fifty")
