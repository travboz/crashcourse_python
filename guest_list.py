# creating a list
guests = ["me", "you", "him"]

print(f"Good morning {guests[0]}, you have been invited to celebrate the celebration with whomever it may concern.")
print(f"Good morning {guests[1]}, you have been invited to celebrate the celebration with whomever it may concern.")
print(f"Good morning {guests[2]}, you have been invited to celebrate the celebration with whomever it may concern.")

print("--------------------------------------------")

# modifying a list
print(f"Attention all, unfortunately {guests[1]} cannot make it to the celebration... what a loss.")

guests[1] = "nino"

print(f"Do not fear, {guests[1]} will be attending in his absence.")

print("--------------------------------------------")

print(f"The list has been updated and now {guests[0]}, you have been invited to celebrate the celebration with whomever it may concern.")
print(f"The list has been updated and now {guests[1]}, you have been invited to celebrate the celebration with whomever it may concern.")
print(f"The list has been updated and now {guests[2]}, you have been invited to celebrate the celebration with whomever it may concern.")


# further modifying a list by inserting at an index, and adding onto the end
guests.insert(0, "jbl")
guests.insert(2, "minor")
guests.append("adage")

print("--------------------------------------------")

print(f"New additions have been made to the guest list and now {guests[0]}, you have been invited to celebrate the celebration with whomever it may concern.")
print(f"New additions have been made to the guest list and now {guests[2]}, you have been invited to celebrate the celebration with whomever it may concern.")
print(f"New additions have been made to the guest list and now {guests[len(guests)-1]}, you have been invited to celebrate the celebration with whomever it may concern.")

print("--------------------------------------------")

# removing guests from our list while being able to access their information
print("To our dismay, the dinner table has arrived and is smaller than we'd expected. As a result of this, we will only be able to invite two guests.")
print(f"{guests.pop()}, sadly you have have been removed from the guest list... :(")
print(f"{guests.pop()}, sadly you have have been removed from the guest list... :(")
print(f"{guests.pop()}, sadly you have have been removed from the guest list... :(")
print(f"{guests.pop()}, sadly you have have been removed from the guest list... :(")

print(f"This leaves {guests} as our honoured guests to celebrate with.")

# removing another way
del guests[1]
del guests[0]

print("--------------------------------------------")

print("The global economy has collapsed and we are now unable to celebrate and hence, no one is invited.")
print(guests)

print(f"The number of guests is now... {len(guests)}.")