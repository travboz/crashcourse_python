sandwich_orders = ["po-boy", "american sub", "bocadillo",
                   "croque-monsieur", "dagwood",
                   "fluffernutter", "francesinha"]

finished_sandwiches = []
order_no = 1

while sandwich_orders:
    currently_making = sandwich_orders.pop()

    print(f"{order_no}: Current making a {currently_making}...")
    finished_sandwiches.append(currently_making)
    order_no += 1

print("All sandwiches have been made.")
print(finished_sandwiches)