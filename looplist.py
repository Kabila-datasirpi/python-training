
fruits=["apple","cherry","banana","orange"]
for i in fruits:
    print(i)

#break in looplist
cars=["audi","maruthi","bmw","mahendra"]
for t in cars:
    print(t)
    if t=="maruthi":
        break

#adjancy
foods=["rice","chappathi","dosa",]
ingredients=["floor","doe","paper"]
for k in foods:
    for j in ingredients:
        print(k,j)
    
    #Dictionaries

k={
    "car":"volvo",
    "year":1999,
    "electic":False,
    "colors":["red","green","blue"]

}
print(k)

#another way of declaring dict
thisdict=dict(name="abi",age=19,school="msuniversity")
print(thisdict)

#access key values
print(k.keys())
print(k.values())

#change items in the dict
k["year"]=2000
print(k)

#using update method to change values
k.update({"year":2002})
print(k)

#add items in the dict
k["num"]=15
print(k)

#remove dict
k.pop("num")
print(k)

#using del
del k["colors"]
print(k)

#using clear
k.clear()
print(k)



