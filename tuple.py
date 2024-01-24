#tuple can be any datatype
a=("apple",1,True)
print(a)

#using tuple constructor 
b=tuple(("cherry",2,False))
print(b)

#change tuple values
lap=("del","lenovo","apple","hp")
clap=list(lap)
clap[1]="panasonic"
lap=tuple(clap)
print(lap)

#add tuple
fruits=("kiwi","orange","papaya")
cfruits=list(fruits)
cfruits.append("guva")
fruits=tuple(cfruits)
print(fruits)

#tuple+tuple
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
tuple3=tuple1+tuple2
print(tuple3)

#remove tuple
y=("car","bus","van","lorry")
z=list(y)
z.remove("lorry")
print(tuple(z))

#unpack tuples
planet=("star","moon","light")
(yellow,red,green)=planet
print(yellow)
print(red)
print(green)

#loop the tuple
for i in planet:
    print(i)

#while loop
    cards=("queen","king","spade")
    v=0
    while v<(len(cards)):
        print(cards[v])
        v=v+1

#multiply tuple
    c=tuple1*2
    print(c)
        

