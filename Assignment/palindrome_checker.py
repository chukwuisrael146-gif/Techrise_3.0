# Palindrome Checker

my_list = ["mummy", "hannah", "murder for a jar of red rum", "mom" "seagull", "tomato", "no lemon no melon", "some men interpret nine memos", "madam"]

for item in my_list:
    # clean the string: remove spaces and commas, convert to lowercase
    neat = item.lower().replace(" ", "").replace(",", "")

    # checking palindrome 
    if neat == neat[::-1]:
        print(f"{item} is a Palindrome")
    else:
        print (f"{item} is not a Palindrome")
        
 
 
# expected out put
# mummy is not a Palindrome
# hannah is a Palindrome
# murder for a jar of red rum is a Palindrome
# momseagull is not a Palindrome
# tomato is not a Palindrome
# no lemon no melon is a Palindrome
# some men interpret nine memos is a Palindrome
# madam is a Palindrome


import time

list1 = []
list2 = []

# Function to collect list input
def get_list(list_name):
    result = []

    while True:
        value = input(f"Enter item for {list_name}: ")
        result.append(value)

        done = input("Are you through? (yes/no): ").lower()

        while done not in ["yes", "no"]:
            done = input("Please enter 'yes' or 'no': ").lower()

        if done == "yes":
            break

    return result


# Get first list
print("FILLING LIST 1")
list1 = get_list("List 1")

# Get second list
print("\nFILLING LIST 2")
list2 = get_list("List 2")

# Check lengths
if len(list1) != len(list2):
    print("\nlength of lists don't match")
    exit()

else:
    print("\nlengths match. Proceeding")

    # Print dots one second apart
    for _ in range(3):
        print(".")
        time.sleep(1)

    # Create dictionary AFTER loop finishes
    result_dict = dict(zip(list1, list2))

    print("\nFinal Dictionary:")
    print(result_dict)