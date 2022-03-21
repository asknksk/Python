"""
Problem : If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?
"""
principal = 1000

day_profit = 0.07

new_principal = principal * ((1 + day_profit)**7)

print(new_principal)

# Output => 1605.7814764784307