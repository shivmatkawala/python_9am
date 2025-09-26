# STRING:-

# What is String ?
    # alphabetic charecters, numbers, special charecters,
    # emojis or anything written inside quotes in python
    # is nothing but a string.
    
# what is quotes ?
    # ''   --> single quotes
    # ""   --> double quotes
    # ''' ''' ---> tripple single quotes
    # """ """ ---> tripple double quotes
    
# why these many quotes ?
    # In english grammer quotes are used to emphasize
    # a particular, specific part of sentence specially
    # adjectives and adverbs.
    
    # Examples:-
        # Karishma is the most 'beautiful women' in our class. 
        # Sai is the "strongest student" in our class.
        # I was going to a temple, i met charan near temple,
        # he was upset. i asked him '''How are you ?'''.
        # He replied """I am not good"""
        
        
# str1 = 'apple'
# print(str1)
# print(type(str1))

# print("--------------------------")

# str2 = "Grapes"
# print(str2)
# print(type(str2))

# print("--------------------------")

# str3 = '''Pineapple'''
# print(str3)
# print(type(str3))

# print("--------------------------")

# str4 = """Watermelon"""
# print(str4)
# print(type(str4))

# print("--------------------------")

# str5 = "Karishma is the most 'beautiful women' in our class."
# print(str5)
# print(type(str5))

# print("--------------------------")

# str6 = 'Sai is the "tallest man" in our class'
# print(str6)
# print(type(str6))

# print("--------------------------")

# str7 = '''Hello dear friend 'tejes', I have been searching for you since "ages".'''
# print(str7)
# print(type(str7))

# print("--------------------------")

# str8 = """'''Woww..! This is awesome. I have been waiting for this.''' rama replied """
# print(str8)
# print(type(str8))
################ INDEXING ###########################

# str11 = 'APPLE'

# Positive Indexing
# print(str11[0])
# print(str11[1])
# print(str11[2])
# print(str11[3])
# print(str11[4])

# Negative Indexing
# print(str11[-5])
# print(str11[-4])
# print(str11[-3])
# print(str11[-2])
# print(str11[-1])


####################### SLICING ##############################
# str12 = "PINEAPPLE"
# print(str12[0:4:1])

################ STRING IN BUILT METHODS ###############

# CASE CONVERSION METHODS:-

# str1 = "apple"    # lowecase
# str2 = "Amma@123"
# str3 = 'PYTHON'
# # .upper()
# print(str1.upper())  #APPLE
# print(str2.upper())  #AMMA@123
# print(str3.upper())  #PYTHON

# str1 = "APPLE"
# str2 = 'ANDYshandy@123'
# str3 = 'power'
# # .lower()
# print(str1.lower())  #apple
# print(str2.lower())  #andyshandy@123
# print(str3.lower())  #power

# str1 = 'i am a diso dancer.'
# str2 = 'i AM a DiscO DANcer'
# str3 = 'you Stay aT road 23@downtown'
# # .capitalize()
# print(str1.capitalize())  #I am a diso dancer.
# print(str2.capitalize())  #I am a disco dancer.
# print(str3.capitalize())  #You stay at road 23@downtown

# str1 = 'gama is a ray'
# str2 = 'i HaVE 200 Ruppes'
# str3 = 'Man Is A Man'

# # .title()
# print(str1.title())  #Gama Is A Ray
# print(str2.title())  #I Have 200 Ruppes
# print(str3.title())  #Man Is A Man


# .swapcase()
# str1 = 'APPLE grapes'
# str2 = 'pYtHoN'
# print(str1.swapcase())  #apple GRAPES
# print(str2.swapcase())  #PyThOn


# SEARCH & REPLACE METHODS:-

# str1 = 'PYTHON'

# # .find()
# print(str1.find('T')) #2
# print(str1.find('O')) #4
# print(str1.find('y')) # -1  --> when no match found
# print(str1.find('HO')) #3
# print(str1.find('YH')) #-1  --> 'YH' substring not found together

# str2 = 'RGvGR'
# print(str2.find('R'))  #0
# print(str2.find('G'))  #1


# .rindex()
# print(str2.rfind('R')) #4
# print(str2.rfind('G')) #3


# str3 = 'RGvRGvRGv'
# print(str3.find('R')) # 0
# print(str3.rfind('R')) # 6


# str1 = 'Apple'
# .index()

# print(str1.index('l')) #3
# print(str1.index('p')) #1
# print(str1.rindex('p')) #2
# print(str1.index('z'))  #ValueError: substring not found

