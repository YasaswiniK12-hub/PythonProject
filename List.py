# A structure in python. Organized data .
# Give your list a name
# [] makes python think like ohh you wanna store bunch of values
friends = ["Shalini", "Sahithi", "Yasaswini", "Joy"]
# 0-indexing
# individual access
# python is fine with you entering any kind of datatype. [Integer, Float, String, Boolean] FINE all good
print(friends)
print(friends[0])
# cool thing . I can access it from the end. NOTE: INDEXING STARTS FROM -1
print(friends[-1])
# from index x to y how ???
print(friends[1:])
print(friends[0:3])
# observe end index . prints element till 1 less than mentoned index
# change a specific value
friends[1]="Amul"
print(friends)

# LIST FUNCTIONS

lucky_numbers =[ 4,8,15,16,23,42]
friends=["Kevin","Karen","Jim","Oscar","Toby"]
  #friends.extend(lucky_numbers)
#  Add two lists together
print(friends)
friends.append("Logan")
print(friends)
# APPEND: ADDS X ONE ELEMENT. AT THE END OF THE LIST
# EXTEND: ADDS EACH ELEMENT INSIDE X ONE BY ONE
# WHAT IF I WANT TO ADD IT SOMEWHERE IN THE MIDDLE
friends.insert(1,"Kelly")
print(friends)
# remove
friends.remove("Jim")
print(friends)
# clear(): get rid of every element in the friends
#friends.clear()
#print(friends)
friends.pop()
print(friends)
# pop(): pops the last element in the list
print(friends.index("Toby"))
friends.append("Kevin")
print(friends.count("Kevin"))
# count(): counts the duplicate values
friends.sort()
# sort(): default ascending order. Here alphabetic order
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
# we can reverse a list
lucky_numbers.reverse()
print(lucky_numbers)
# copy(): Copy the list
friends2=friends.copy()
print(friends2)