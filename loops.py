# for variables in collection:
    #this block runs once for each item in the collection
    # <variable> holds the current item on each iteration
    
#Tis is the list used in for loop example

# scores = [70, 30, 50, 45, 60]
# for score in scores:
#     print(f"This is your score: {score + 2}")
    
# for i in range(1,101):
#     if i % 3 == 0:
#         print(i)
        
""" 
initialize a list called name and assign three names to it then use a for loop statement that says good morning to each of the names
"""

# names = ["Chimereucheya", "Goodness", "Daniel"]
# for name in names:
#     print(f"Good Morning {name}")
    
# # words = input("Enter a word: ")
# # vowel = "aeiou"

# # for vowels in words:
# #     if vowels.lower() in vowel:
# #         print(vowels)
        
# # using for loop in dictionary
# db_config = {
#     "host": "db.techrise.ng",
#     "port": 5432,
#     "name": "analytics_db",
#     "max_conections": 50
# }


# for key in db_config:
#     print(key) 
    
# for value in db_config.values():
#     print(value)

# for key, values in db_config.items():
#     print(f"{key} : {values}")
    
# db_config = {
#     "host": ["db.techrise.ng", "Red"],
#     "port": [5432, 564],
#     "name": ["analytics_db", "Simple"],
#     "max_conections": [50, 50]
# }

# Nested for Loop

# for key, values in db_config.items():
#     print(values)
#     for value in values:
#         print(value)
        # print(f"{key}: {values}")

# while <condition>:
    #This block runs repeatedly as long as condition is True
    #Critical: something in this block must eventually make
    #the condition False, or the loop will run forever!
    
# count = 0
# while count <= 4:
#     print("We have eaten lunch")
#     count += 1
    
    
# command = ""

# while command != "exit":
#     command = input("Give me a command: ")

# count = 1
# ages = []
# while count <= 5:
#     user_age = input("How old are you?: ").strip()
#     if user_age.isdigit():
#         ages.append(user_age)
#         count +=1
#     else:
#         print("write your age in figure")
# print(ages)
# for age in ages:
#     print(f"I am {age} years old.")

# using break statemnt
# while count <= 5:
#     user_age = input("How old are you?: ").strip()
#     if user_age.isdigit():
#         ages.append(user_age)
#         count +=1
#     else:
#         print("write your age in figure")
#         break
# print(ages)
# for age in ages:
#     print(f"I am {age} years old.")
    
    
# --- Break : stop as soon as a problem is found --- 
# pipeline_stages = ['extract', 'transform', 'validate', 'load']
# faild_stage = 'validate'

# for stage in pipeline_stages:
#     print(f"Running stage: {stage}")
#     if stage == faild_stage:
#         print(f"FALIURE at stage '{stage}'. Stopping pipline. ")
#         break # Exit the loop immediately
    
# --- CONTINUE: skip null/missing records ---
# records = [
#     {"id": 1, "value": 500},
#     None,  # corrupt/missing record
#     {"id": 3, "value": 750},
#     None,
#     {"id": 5, "value": 300}
# ]

# total = 0
# for record in records:
#     if record is None:
#         # print("skipping null record...")
#         continue #skip iteration to be the next record
#     total += record["value"]
    
# print(f"Total value of valid recods: {total}") # 1550

# functions

# def   -> keyword telling python you're defining a function
# name -> meaningul identifier (use snake_case: get_user_by_id )
# parameters -> inputs the funtion needs (in parantheses)
# body  -> the indented block of code that runs when called
# return -> sends a result to whoever called the function

# def greet_User(name):       # 'name' is the PARAMETER
#     message = f"Welcome to the platform, {name}!"
#     return message     # Return the result

# result = greet_User("Ada")
# print(result)
# print(greet_User("Tunde"))
# print(greet_User("femi"))

def greet_User(name):       # 'name' is the PARAMETER
    message = f"Welcome to the platform, {name}!"
    print(message)    # Return the result

