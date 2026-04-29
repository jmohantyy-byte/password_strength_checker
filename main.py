# Password Strength Checker

password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters long")

# Check uppercase letter
if any(char.isupper() for char in password):
    score += 1
else:
    print("Add at least one uppercase letter")

# Check lowercase letter
if any(char.islower() for char in password):
    score += 1
else:
    print("Add at least one lowercase letter")

# Check numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    print("Add at least one number")

# Check special characters
special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(char in special_characters for char in password):
    score += 1
else:
    print("Add at least one special character")

# Final result
print("\nPassword Strength Result:")

if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")