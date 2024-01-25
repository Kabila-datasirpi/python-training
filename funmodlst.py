def modify(lst):
    lst.append("van")
    lst[4]="omni"
    return(lst)


list=["car","bus","lorry","train"]
modify(list)
print(list)
