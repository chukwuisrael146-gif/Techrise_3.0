# list
# list conprehension
# tuple



list1 = ["age", "food", "beans", "dance", "apple"]
list2 = ["buns", "barb", "sololucky" "fan"]

# join = list1 + list2
# print(join)

# list1.insert(1, "food")
# print(list1)
# list1.insert(2, "goodness")
# print(list1)
# list1.extend(list2)
# print(list1)

# newlist = [expression for itemin iterable if condition == True]         # syntax for list comprehension

result = [list1[i] for i in range(len(list1)) if i % 2 == 1]
print(result)

# for numbers 0-50 that are divisible by 5 add them to a particular list
numbers = []
num = [num for num in range(51) if num % 5 == 0]
numbers.append(num)
print(numbers)

thistuple = ("food", "dance", "ballon")
var1 = tuple((list1))
print(var1)
print(type(var1))
print(thistuple)
print(type(thistuple))
print(len(thistuple))


# sets 
settings = {"apple", "orange", "banana", "apple", "strawberry", "lemon", "lemon", "melon", "grapes"}
print(settings)

my_dict = {"name": "John", 
           "age": 20, 
           "city": "Lagos"}

for key, value in my_dict.items():
    print(key, ":", value)
    
    
print(my_dict.get("age"))