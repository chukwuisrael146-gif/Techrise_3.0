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