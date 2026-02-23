# Temperature Monitoring System

temperatures = [32, 45, 41, 38, 47, 29, 42, 46]

hottest = max(temperatures)
coldest = min(temperatures)

# Count extreme days (> 40)
extreme_days = len([t for t in temperatures if t > 40])

# Replace > 45 with "Heat Alert"
for i in range(len(temperatures)):
    if temperatures[i] > 45:
        temperatures[i] = "Heat Alert"

print("Hottest Day:", hottest)
print("Coldest Day:", coldest)
print("Extreme Days (>40°C):", extreme_days)
print("Updated Temperature List:", temperatures)