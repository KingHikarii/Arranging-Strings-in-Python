
max = int(input("Enter a number to be the maximum: "))
list = []

for i in range(max):
    word = input("Enter a word: ")
    list.append(word)

print("Unsorted list: ",list)
newList = sorted(list)
print("Sorted list:",newList)

print("Recovering the first and last word within the sorted list: ")
print("The first word is: ", newList[0])
print("The last word is: ", newList[len(newList)-1])