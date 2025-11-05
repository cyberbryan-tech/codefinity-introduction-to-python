# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice the `items` string into individual items
candy1 = items[:9]        # Bubblegum
candy2 = items[11:20]     # Chocolate
dry_goods = items[22:]     # Pasta

# Slice the `categories` string into individual categories
category1 = categories[:11]   # Candy Aisle
category2 = categories[13:]   # Pasta Aisle

# Price variables must be strings with "$"
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# Print using variables (and lowercase to match expected output)
print("we have " + candy1.lower() + " for " + bubblegum_price + " in the " + category1.lower())
print("we have " + candy2.lower() + " for " + chocolate_price + " in the " + category1.lower())
print("we have " + dry_goods.lower() + " for " + pasta_price + " in the " + category2.lower())