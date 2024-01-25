#read the file
f=open("/home/datasirpi/sample","r")
print(f.read())

#read first five characters
print(f.read(5))

#readline
print(f.readline())

#close the file
f.close()

#append
t=open("/home/datasirpi/sample","a")
t.write("now the file contain more info")
print(t.read())

#write
s=open("/home/datasirpi/sample","w")
s.write("oops I have deleted some content")
print(s.read())




