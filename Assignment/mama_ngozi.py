bulk_order = 800.00 # 10 or more
group_order = 1000.00 # 5 to 9
standard_price = 1200.00  # 2 to 4
single_portion = 1500.00  # just 1
no_order = "Please enter a valid number"  # 0 or less

# Asking the user for the number of portions with while loop
while True:
    order = int(input("Order any portion of Jollof Rice: "))

    # Calculating the price and label
    if order >= 10:
        total_price = order * bulk_order
        label = "Bulk order - big discount!"
        print(f"Total: #{total_price} - {label}")
        break
    elif order >= 5:
        total_price = order * group_order
        label = "Group order - small discout!"
        print(f"Total: #{total_price} - {label}")
        break
    elif order >= 2:
        total_price = order * standard_price
        label = "Standard price."
        print(f"Total: #{total_price} - {label}")
        break
    elif order >= 1:
        total_price = order * single_portion
        label = "Single portion - premium price."
        print(f"Total: #{total_price} - {label}")
        break
    else:
        print(no_order)
# print the result if the input is valid
# print(f"Total: #{total_price} - {label}")