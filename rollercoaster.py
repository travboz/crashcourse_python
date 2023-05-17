# like C, input is all strings
# so we need to convert to int for int input, e.g:
prompt = "How tall are you, in cm? "
height = input(prompt)
height = int(height)

if height >= 120:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")