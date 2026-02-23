# Bank Transaction Analyzer

transactions = [20000, -5000, 15000, -12000, 8000, -2000]

# Total balance
total_balance = sum(transactions)

# Largest withdrawal (most negative value)
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

# Deposits greater than 10000
large_deposits = len([t for t in transactions if t > 10000])

print("Total Balance: ₹", total_balance)
print("Largest Withdrawal: ₹", largest_withdrawal)
print("Deposits > ₹10000:", large_deposits)