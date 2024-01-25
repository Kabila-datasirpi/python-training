#reading line by line in files
f=open("/home/datasirpi/samp","r")
lines=f.readlines()
 
count=0
for line in lines:
    count+=1
    print("line{}:{}".format(count,line.strip()))
f.close()
 
 
 
#writing multiple line
k=open("file.txt","w")
lines=["welcome\n","everyone\n","in this group\n"]
k.writelines(lines)
print(k)
k.close()