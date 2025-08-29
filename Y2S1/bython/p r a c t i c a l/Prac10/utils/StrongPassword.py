from utils.Password import Password

class StrongPassword(Password):
    """
    Represents a strong password, extending the base Password class.
    Adds three additional validation rules:
    1. Must be at least 12 characters long.
    2. Must include at least one uppercase letter.
    3. Must include at least one lowercase letter.
    """
    def __init__(self, password_str=""):
        super().__init__(password_str)

    def validate(self):
        errors = super().validate()

        password = self.get_password()
        
        if len(password) < 12:
            errors.append("Error: The password must have at least 12 characters.")
            
        has_upper = False
        has_lower = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
        
        if not has_upper:
            errors.append("Error: The password must include uppercase characters.")
        
        if not has_lower:
            errors.append("Error: The password must include lowercase characters.")
            
        return errors
