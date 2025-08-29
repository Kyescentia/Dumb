from utils.StrongPassword import StrongPassword

validated_password = ""

while True:
    password_input = input("Enter a password: ")
    strong_pass = StrongPassword(password_input)
        
    error_list = strong_pass.validate()
        
    if not error_list:  
        print("Password has been validated successfully.")
        validated_password = password_input
        break
    else:
        for error in error_list:
            print(error)
        print()

while True:
    confirmation = input("Enter the same password again: ")
    if confirmation == validated_password:
        print("Congratulations! Your password is created successfully!")
        break
    else:
        print("Error: Passwords do not match. Please try again.")