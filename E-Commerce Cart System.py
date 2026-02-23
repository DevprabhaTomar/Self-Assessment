# E-Commerce Cart System

prices = [1200, 2500, 1200, 800, 3000, 800]

# Remove duplicate items
unique_prices = list(set(prices))

total = sum(unique_prices)

# Apply 10% discount if total > 5000
if total > 5000:
    discount = total * 0.10
else:
    discount = 0

total_after_discount = total - discount

# Add 18% GST
gst = total_after_discount * 0.18
final_amount = total_after_discount + gst

print("Unique Prices:", unique_prices)
print("Final Payable Amount: ₹", round(final_amount, 2))