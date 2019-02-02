#lists are modifiable
#objects of class index
list1 = [1,"ali",4]
print(list1)

#tuples are not modifiabe
#objects of class tuple
tup = (1,2,3)
print(tup.index(3))
print(tup.count(1))


#dictionaries store data in key value format
#value can be a list, number, string
#key can be a string or number

dic1 = {
    "Ali":23,
    "Zara":34,
    "Waseem":54
    }
print(dic1)

#deleting element form list / dictionories
#del   list_name [ index ] 
del list1[0]
print(list1)
#del dict_name[ key ]
del dic1["Ali"]
print (dic1)
