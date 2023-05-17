from pathlib import Path

path = Path("guest.txt")
guest_name = input("To see if you are on the guest list, pleas enter your name: ")

path.write_text(guest_name)