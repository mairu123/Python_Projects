# Student Profile Management System with Login


# stores user signup details
user_Signup_Details = {}

# Student profile storage
student_profiles = []

# Signup Function that take username and password
def signup():
    print("\n Sign Up ")
    username = input("Enter a new username: ")
    if username in user_Signup_Details:
        print(" Username already exists. Try logging in.")
        return False
    password = input("Enter a new password: ")
    user_Signup_Details[username] = password
    print("Signup successful! Please login to continue.")
    return False

# Login Function that checks username and password and matches with signup details
def login():
    print("\n Login ")
    username = input("Username: ")
    password = input("Password: ")
    if user_Signup_Details.get(username) == password:
        print(" Login successful. Welcome,", username)
        return True
    else:
        print(" Invalid credentials. Try again.")
        return False

signup()
login()

