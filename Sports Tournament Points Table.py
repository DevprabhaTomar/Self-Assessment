# Sports Tournament Points Table

# Format: Team : [wins, draws, losses]
teams = {
    "Team A": [5, 2, 1],
    "Team B": [4, 3, 1],
    "Team C": [6, 0, 2],
    "Team D": [3, 2, 3]
}

points_table = {}

for team, record in teams.items():
    wins, draws, losses = record
    points = wins * 3 + draws * 1
    points_table[team] = points

# Sort by points descending
sorted_table = sorted(points_table.items(), key=lambda x: x[1], reverse=True)

print("🏆 Points Table")
for team, points in sorted_table:
    print(team, ":", points, "points")