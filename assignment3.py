
## PYTHON ASSIGNMENT 
# set operator
set={'apple','banana','grapes','orange','mango'}
print(set)

# adding one element
set.add("lemon")
print(set)

# removing fruits
set.remove('apple')
print(set)

#to check specific fruit is in the set

if 'banana' in set:
    print("banana in set")
else:
    print("banana not in set")


## dictionary

dict={'name':"ram",'age':20,"accupation":"doctor"}
print(dict)

#to add one pair into dict
dict.update({"location":"hyderabad"})
print(dict)

# to update the value
dict["age"]=30
print(dict)

# to print persons occupation
print(dict["accupation"])

# python  function to remove duplicates using set
def remove_duplicates(numbrs):
    return set(numbers)
num=[1,2,4,5,6,2,3,2]
rusult=remove_duplicates(nums)
print("after removing duplicates",result)    


