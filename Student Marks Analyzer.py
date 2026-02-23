# Student Marks Analyzer

# Input list of marks
marks = [85, 92, 78, 105, -5, 88, 92, 67]

# Step 1: Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

if not valid_marks:
    print("No valid marks available.")
else:
    # Step 2: Calculate average
    average = sum(valid_marks) / len(valid_marks)

    # Step 3: Find topper(s)
    highest = max(valid_marks)
    toppers = [m for m in valid_marks if m == highest]

    # Step 4: Assign grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    # Display results
    print("Valid Marks:", valid_marks)
    print("Average Marks:", round(average, 2))
    print("Highest Marks (Topper(s)):", toppers)
    print("Grade Based on Average:", grade)