"""
1. Take an input asking the user to enter a score
2. Return A if the user code is 70 and above 
Return B if the user's score is between 60 and 69 (inclusive)
Return C if the user's score is btw 50 and 59 (inclusive)
Return D if the user's score is btw 40 and 49 (inclusive)
Return E if the user's score is btw 30 and 39 (inclusive)
Return F if less than 30 
"""

score = float(input("Enter Your Score "))

if score >= 70 and score <= 100:
    print ("Grade: A")
elif score >= 60 and score <= 69:
    print("Grade: B")
elif score >= 50 and score <=59:
    print("Grade: C")
elif score >= 40 and score <= 49:
    print("Grade: D")
elif score >= 30 and score <= 39:
    print("Grade: E")
elif score >= 0 and score < 30:
    print("Grade: F")
else:
    print(f"Invalid Score {score}\nMust be Btw 0 and 100")