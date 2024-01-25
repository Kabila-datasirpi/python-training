#using append method to add items in the list
list=["apple","banana","cherry","strawberry"]
list.append("mango")
print(list)

#using insert method to add items in the particular index
list.insert(3,"guva")
print(list)

#extend list
cars=["volo","bmw"]
cars2=["audi","mehendra"]
cars.extend(cars2)
print(cars)

#remove list items
cars.remove("bmw")
print(cars)

#using pop
cars.pop()
print(cars)  #we can specify the index no in the round braces to pop an particular index value

#sort in list
cars.sort()
print(cars)

#reverse in list
cars.reverse()
print(cars)

