number_of_pizzas = int(input('How many pizzas do you want?'))

cost_per_pizza = int(input('How much does a pizza cost?'))

subtotal = number_of_pizzas * cost_per_pizza

tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

print(f'Full cost: {total}$')
print(f'Including for pizza: {subtotal}$')
print(f'Tax: {sales_tax}$')