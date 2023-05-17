usernames = ("carlos1", "newb2", "bigmumma3", "admin", "horis4")

# for username in usernames:
#     if username == "admin":
#         print("Good morning sir.")
#     else:
#         print(f"Good morning {username}")

usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Good morning sir.")
        else:
            print(f"Good morning {username}")



current_users = ["tom", "paul", "mario", "tony", "frank"]
new_users = ["tony", "harry", "harold", "maud", "vader", "frank"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} is currently in use. Please enter a different username.")
    if new_user.lower() not in current_users:
        print(f"{new_user} is available.")


