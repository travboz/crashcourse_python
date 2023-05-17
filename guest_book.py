from pathlib import Path

path = Path("guest_book.txt")
guest_book = []

print("This is the guest list checker. Enter 'quit' at any point to exit.")

while True:
    guest_name = input("To see if you are on the guest list, pleas enter your name: ")

    if guest_name.lower() == 'quit':
        break
    else:
        guest_book.append(guest_name)

guest_print = ''
for guest in guest_book:
    guest_print += f"{guest}\n"

path.write_text(guest_print)

