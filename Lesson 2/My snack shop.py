#========================
# My Snack Shop
# File:my-snack-shop.py
#========================


# Parts 1 - TYPES OF DATA
snack_name = "Chips"   # str  - text
price = 1.50     # float - decimal 
quantity = 10           # int   - whole number
is_available = True    # bool  - True or False

print("Snack Name:", snack_name)
print("Snack Price:", price)
print("In Stock:", quantity)
print("Is Available:", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))


# Part 2 - ARITHMETIC OPERATORS
total = price * quantity
print("Total value: $", total)
print("Sale price: $", price * 0.25) 
print("double stock:", quantity * 2)


# Part 3 - COMPARISON OPERATORS
print("is price under $2.00?", price < 2.00)
print('more than 5 in stock?', quantity > 5)
print("is price equal to $1.50?", price == 1.50)


# Part 4 - STRING OPERATORS
shop_name = "Mumin's Snack Shop"
print("Shop Name:", shop_name)
print("letters in snack_name:", len(snack_name))
print("First letter:", snack_name[0])


# Part 5 - SWAPPING VALUES
price_a = 1.50
price_b = 3.00
print("before", price_a, "and", price_b)


temp = price_a
price_a = price_b
price_b = temp

print("after", price_a, "and", price_b)
