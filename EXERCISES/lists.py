#create list
thisList = ["Jane", "Naom", "sylvia"]
print(thisList)

#Using list() constructor to create a list
list2 = list(("Ann", 50, True))#use double round brackets
print(list2)

#Duplicates
thislist = ["Jane", "Naom", "Ann", "Jane"]
print(thislist)

#List Length
print(len(thislist))

#Different datatypes
list1 = ["abc", True, 10, False, "Jane"]
print(list1)

#Datatype of a list
print(type(list1))


#Accessing List items
list3 = ["Apples", "Oranges", "Pineapples", "lemons"]
print(list3[0])#first item
print(list3[-1])#last item
print(list3[1:])#second,third and fourth items
print(list3[0:2])#firstand second items
print(list3[:3])#all items from the beginning but not including the last item
print(list3[-3:-1])

#Check if item exists
list4 = [2,6,5,3,9]
if 5 in list4:
    print("5 is a number.")

if "True" not in list4:
    print("\"True\" is not a number.")



#Change list items
fruits = ["bananas", "grapes", "kiwi", "mangoes"]
fruits[1] = "Oranges"
print(fruits)

colours = ["red", "Green", "Yellow", "Blue", "Purple"]
colours[1:4] = ["Black", "Violet", "Indigo"]
print(colours)


students = ["Felix", "Dickson", "Kevin"]
students[0:1] = ["John", "James", "Jeff"]
print(students)


members = ["Dickson", "kevin", "Leon"]
members[0:] = ["Felix"]
print(members)



#Insert items
list5 = ["carrots", "kales", "brocolli", "cabbage"]
list5.insert(1,"tomatoes")
print(list5)



#Append items
list6 = [10, 20, 30, 40, 50]
list6.append(70)
print(list6)



#Extend list
#Add elements of another list to the current list
list7 = [2, 4, 6, 8]
list8= [1, 3, 5, 7, 9]
list7.extend(list8)
print(list7)

#Add elements of any iterable object i.e sets, tuples and dictionaries
thislist = ["lion", "ape", "tiger", "deer"]
thistuple = ("elephant", "leopard", "hyena")
thislist.extend(thistuple)
print(thislist)



#Remove items
#Remove specified element
thislist = ["Apple", "Avocado", "Banana"]
thislist.remove("Avocado")
print(thislist)


#Remove the first occurence of duplicate items
thislist = ["bicycle", "bus", "train", "aeroplane", "car", "bus"]
thislist.remove("bus")
print(thislist)


#remove specified index
thislist = ["Oranges", "Apple", "Mangoes"]
thislist.pop(1)
print(thislist)


thislist.pop()#removes the last item
print(thislist)


#del keyword
thislist = [300, 50, 23, 5, 67, 39]
del thislist[0]#removes the first element
print(thislist)


del thislist #deletes the list completely

#Clear the list - empties the list 
thislist = ["red", "yellow", "green"]
thislist.clear()
print(thislist)



#Loop lists
thislist = ["watermelon", "lemon", "mango"]
for x in thislist:
    print(x)


thislist = ["orange", "green", "pink", "violet"]
[print(x) for x in thislist]    



for i in range(len(thislist)):
    print(thislist[i])    



list1 = ["tomato", "potato", "carrot", "onion", "letuce"]
i = 0
while i<len(list1):
    print(list1[i])
    i = i+1



#list comprehension
#without comprehension
fruits = ["Guavas", "strawberry", "passionfruit", "dragon fruit"]
newlist = []
for x in fruits:
    if "o" in x:
        newlist.append(x)#prints only elements with "o"
print(newlist)    


#with comprehension
fruits = ["Guavas", "strawberry", "passionfruit", "dragon fruit"]
newlist=[x for x in fruits if "o" in x]
print(newlist)



fruits = ["Guavas", "strawberry", "passionfruit", "dragon fruit"]
newlist=[x for x in fruits if x != "strawberry"]
print(newlist)




#create iterable
newlist = [x for x in range(6)]#numbers less than 6 from 0
print(newlist)


newlist = [x for x in range(6) if x>2]#numbers in the range of 6 but greater than 2
print(newlist)


fruits = ["Guavas", "STRAWBERRY", "passionfruit", "dragon fruit"]
newlist=[x.lower() for x in fruits]
print(newlist)

newlist = ["Green" for x in fruits]#set all the values in the list to "Green"
print(newlist)


#Sorting lists