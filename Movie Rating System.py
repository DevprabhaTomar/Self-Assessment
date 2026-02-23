# Movie Rating System

ratings = [5, 4, 3, 6, 2, 5, 0, 1, 5]

# Remove invalid ratings (valid: 1–5)
ratings = [r for r in ratings if 1 <= r <= 5]

average_rating = sum(ratings) / len(ratings)
five_star_count = ratings.count(5)

ratings.sort()

print("Valid Ratings:", ratings)
print("Average Rating:", round(average_rating, 2))
print("Number of 5-Star Ratings:", five_star_count)