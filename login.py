user_name = input("Enter your username: ").title()
password = int(input("Enter your password: "))

if user_name == "Israel" and password == 123456:
    print(f"Welcome {user_name}")
else:
    print("Invalid Credentials")