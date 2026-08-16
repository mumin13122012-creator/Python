# 1. Variables and Data Types
passenger_name = "Alex"      # string
tickets_count = 3            # integer
price_per_ticket = 45.50     # float
is_round_trip = True         # boolean

print("--- Booking Info ---")
print("Passenger Name:", passenger_name)
print("Number of Tickets:", tickets_count)
print("Price per Ticket: $", price_per_ticket)
print("Round Trip:", is_round_trip)
print()

# 2. Arithmetic Operators
total_cost = tickets_count * price_per_ticket
discount = 10.00
final_price = total_cost - discount

print("--- Pricing Details ---")
print("Total Cost: $", total_cost)
print("Discount Applied: $", discount)
print("Final Price: $", final_price)
print()

# 3. Comparison Operators
budget = 120.00
is_within_budget = final_price <= budget
is_vip_destination = passenger_name == "Alex"

print("--- Comparisons ---")
print("Is final price within budget?", is_within_budget)
print("Is VIP passenger?", is_vip_destination)
print()

# 4. String Operations
destination = "Paris Express"

print("--- String Manipulation ---")
print("Uppercase Destination:", destination.upper())
print("Lowercase Destination:", destination.lower())
print("Destination Length:", len(destination))
print("First Character:", destination[0])
print("Concatenated String:", passenger_name + " is travelling via " + destination)
print()

# 5. Variable Swapping
ticket_price_A = 100.00
ticket_price_B = 150.00

print("--- Before Swapping ---")
print("Ticket A:", ticket_price_A, "| Ticket B:", ticket_price_B)

# Swapping two variables in Python
ticket_price_A, ticket_price_B = ticket_price_B, ticket_price_A

print("--- After Swapping ---")
print("Ticket A:", ticket_price_A, "| Ticket B:", ticket_price_B)