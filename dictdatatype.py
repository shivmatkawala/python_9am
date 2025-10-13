# Dictionary:-

    # Initialization:-
# dict1 = {}
# print(dict1)
# print(type(dict1))

# print("---------------------------------------")


# dict2 = {'name': 'sommya', 'age':22, 'city': 'anantpur', 'marks':78}
# print(dict2)
# print(type(dict2))

# print("------------------------------------")

# print(dict2['name'])
# print(dict2['age'])
# print(dict2['city'])
# print(dict2['marks'])


# print("------------------------------------")
# keys = ['fruit', 'cloth', 'city', 'hobby', 'school']
# values = ['Mango', 'shirt', 'kakinada', 'playing games', 'St. Xaviers Shool']

# dict3 = dict(zip(keys, values))
# print(dict3)


# print("---------------------------------------------")

# # dict4 = {'Rohit': 'Fail', 'Sneha':'Fail', 'sameer':'Fail', 'Shabana':  'Fail'}

# studenst = ['Rohit', 'Sneha', 'Sameer', 'Shabana']
# dict4 = dict.fromkeys(studenst, 'Fail')
# print(dict4)


# print("------------------------------------------")

# dict5= {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
# print(dict5)
# print(type(dict5))

# print("------------------------------------------------------------------------------------------")

# Dictionary Methods 
# dict1 = {'One':1,  'Two':2, 'Three':3, 'Four':4}

# # .keys()
# keys = dict1.keys()
# print(keys)
# print(type(keys))  #dict_keys

# print("-------------------------------------------------------------------------")

# list_keys = list(keys)
# print(list_keys)
# print(type(list_keys))

# .values() 
# values = dict1.values()
# print(values)
# print(type(values))

# print("------------------------------------------------------------------------------------------")

# list_values = list(values)
# print(list_values)
# print(type(list_values))

# print("------------------------------------------------------------------------------------------")

# # .items()

# items = dict1.items()
# print(items)
# print(type(items))

# print("------------------------------------------------------------------------------------------")

# list_items = list(items)
# print(list_items)
# print(type(list_items))


# print("------------------------------------------------------------------------------------------")

# dict1 = {'One':1,  'Two':2, 'Three':3, 'Four':4}

# # add pairs
# dict1['Five'] = 5
# dict1['Six'] = 6

# # print(dict1)

# print("------------------------------------------------------------------------------------------")

# dict1['One'] = 100
# dict1['Five'] = 500
# dict1['Seven'] = 700
# # print(dict1)

# dict1.pop('Five')
# dict1.pop('Three')

# # print(dict1)

# dict1.popitem()
# dict1.popitem()
# dict1.popitem()
# dict1.popitem()
# print(dict1)


dict2 =  {1:100, 2:200, 3:300, 4:400, 5:500}
# dict2.clear()
# print(dict2)

print(dict2.get(1))
