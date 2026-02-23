# Salary Processing System

salaries = [25000, 60000, 45000, 80000, 15000, 52000]
minimum_wage = 20000

# Remove salaries below minimum wage
valid_salaries = [s for s in salaries if s >= minimum_wage]

# Add 5% bonus to employees with salary > 50000
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] *= 1.05

# Sort in descending order
valid_salaries.sort(reverse=True)

# Display top 3
top_3 = valid_salaries[:3]

print("Processed Salaries:", valid_salaries)
print("Top 3 Highest Salaries:", top_3)