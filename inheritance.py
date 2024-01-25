#single inheritance
class father():
    f_name="raja"
    f_age=40
class Son(father):
    s_name="kumar"
    s_age=19
obj=Son()
print(obj.f_name)
print(obj.s_name)


#multilevel inheritance
class gf():
    gfname="guru"
    gfage=80
class f(gf):
    fname="mohan"
    fage=50
class s(f):
    sname="praveen"
    sage=22

obj=s()
print(obj.gfname)
print(obj.fname)
print(obj.sname)

#multiple inheritance
class fa():
    faname="guru"
    faage=80
class mo():
    moname="sneha"
    fage=50
class so(fa,mo):
    soname="praveen"
    soage=22

obj=so()
print(obj.faname)
print(obj.moname)
print(obj.soname)

