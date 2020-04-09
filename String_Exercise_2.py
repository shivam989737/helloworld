# Take two comma separated inputs from user
# 1.user's name ' ,ex-"Harshit"
# 2.A single character , "H"
#
# output :
# 1.user's name length'
# 2.count the character that user inputed (bonus :case insensitive count)

username ,single_character=input("Enter the username and single character  : ").split(",")
# print(f"length of the username is :{len(username)}")
print(f"count of character of {single_character} is :{username.lower().count(single_character.lower())}")

