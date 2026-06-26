 
# set operator
set={'apple','banana','grapes','orange','mango'}
print(set)
set.add("lemon")
print(set)
set.remove('apple')
print(set)

if 'banana' in set:
    print("banana in set")
else:
    print("banana not in set")


## dictionary

dict={'name':"ram",'age':20,"accupation":"doctor"}
print(dict)
dict.update({"location":"hyderabad"})
print(dict)
dict["age"]=30
print(dict)
print(dict["accupation"])

# python  function to remove duplicates using set
def remove_duplicates(numbrs):
    return set(numbers)
num=[1,2,4,5,6,2,3,2]
rusult=remove_duplicates(nums)
print("after removing duplicates",result)    


