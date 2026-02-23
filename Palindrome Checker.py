# Palindrome Checker

text = input("Enter a string: ")

# Remove spaces and convert to lowercase
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("It is a Palindrome.")
else:
    print("It is NOT a Palindrome.")