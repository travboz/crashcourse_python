def make_sandwich(*condiments):
    """Creates a sandwich from the condiments provided."""
    print("One slice of bread....")
    print("And now to top with another slice of bread.")
    print("Here is your sandwich with: ")
    for condiment in condiments:
        print(f"- {condiment}")

make_sandwich("cheese", "pastrami", "mustard", "gherkins", "bacon")