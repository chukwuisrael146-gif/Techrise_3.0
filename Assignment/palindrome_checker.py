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


