sandwich_orders = ["po-boy", "american sub", "pastrami", "bocadillo",
                   "croque-monsieur", "pastrami", "dagwood",
                   "fluffernutter", "francesinha", "pastrami"]

finished_sandwiches = []
order_no = 1

while sandwich_orders:
    currently_making = sandwich_orders.pop()
    if currently_making == 'pastrami':
        print("We don't do pastrami!")
        continue

    print(f"{order_no}: Current making a {currently_making}...")
    finished_sandwiches.append(currently_making)
    order_no += 1

print("All sandwiches have been made.")
print(finished_sandwiches)