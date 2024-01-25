#while loop
i=6
while i<=10:
    print(i)
    i=i+1


#continue in while loop
k=10
while k<50:
    k=k+1
    if k==30:
        continue
    print(k)

#break in while loop
l=10
while l<50:
    print(l)
    if l==35:
        break
    l=l+1

#for loop
x="kabila"
for i in x:
    print(i)

#loop in numbers
for c in range(10):
    print(c)

#print num between 5 to 10
for n in range(5,11):
    print(n)

#print numbers 1 to 50 in triple
for j in range(1,50,3):
    print(j)

#break in for loop
for t in range(1,50):
    print(t)
    if t==30:
        break