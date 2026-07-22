# for loop
# this variable letter : used in each iteration. Each time a new value
friends=["Jim","Karen","Kevin"]

for letter in "Giraffe Academy":
    print(letter)
for friend in friends:
    print(friend)
for index in range(10):
    print(index)
# notice it does not print 10
for index in range(3,10):
    print(index)
for index in range(3,10,2):
    print(index)
for index in range(len(friends)):
     print(friends[index])
for index in range(5):
    if index==0:
        print("First Iteration")
    else:
        print("Not first")
